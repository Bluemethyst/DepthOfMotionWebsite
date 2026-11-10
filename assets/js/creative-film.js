/* Start the film quietly in view; retain YouTube's normal manual controls. */
(() => {
  const frame = document.querySelector('#creative-film-embed');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!frame || !('IntersectionObserver' in window) || reducedMotion.matches) return;
  if (!['http:', 'https:'].includes(window.location.protocol)) return;

  const source = new URL(frame.src);
  source.searchParams.set('origin', window.location.origin);
  frame.src = source.href;

  let player;
  let ready = false;
  let visible = false;
  let loading = false;
  let hasPlayed = false;
  let manuallyPaused = false;
  let automaticPause = false;
  let ended = false;

  function pause() {
    if (!ready) return;
    const state = player.getPlayerState();
    if (state === YT.PlayerState.PLAYING || state === YT.PlayerState.BUFFERING) {
      automaticPause = true;
      player.pauseVideo();
    }
  }

  function syncPlayback() {
    if (!ready) return;
    if (!visible || document.hidden) {
      pause();
    } else if (!reducedMotion.matches && !manuallyPaused && !ended) {
      player.playVideo();
    }
  }

  function loadPlayer() {
    if (loading) return;
    loading = true;
    const apiReady = new Promise((resolve, reject) => {
      if (window.YT?.Player) return resolve();
      const previousReady = window.onYouTubeIframeAPIReady;
      window.onYouTubeIframeAPIReady = () => {
        previousReady?.();
        resolve();
      };
      const script = document.createElement('script');
      script.src = 'https://www.youtube.com/iframe_api';
      script.onerror = reject;
      document.head.append(script);
    });
    apiReady.then(() => {
      player = new YT.Player(frame, {
        events: {
          onReady: (event) => {
            player = event.target;
            ready = true;
            player.mute();
            syncPlayback();
          },
          onStateChange: (event) => {
            if (event.data === YT.PlayerState.PLAYING) {
              hasPlayed = true;
              manuallyPaused = false;
              ended = false;
              if (!visible || document.hidden) pause();
            } else if (event.data === YT.PlayerState.PAUSED) {
              if (automaticPause) automaticPause = false;
              else if (hasPlayed && visible && !document.hidden) manuallyPaused = true;
            } else if (event.data === YT.PlayerState.ENDED) {
              ended = true;
            }
          },
          onAutoplayBlocked: () => { manuallyPaused = true; },
        },
      });
    }).catch(() => {
      // The iframe and direct YouTube link remain usable if the API cannot load.
    });
  }

  const observer = new IntersectionObserver(([entry]) => {
    // Separate start/stop thresholds avoid flickering at the viewport edge.
    if (entry.intersectionRatio >= 0.5) visible = true;
    else if (entry.intersectionRatio < 0.2) visible = false;
    if (visible) loadPlayer();
    syncPlayback();
  }, { threshold: [0, 0.2, 0.5] });
  observer.observe(frame);
  document.addEventListener('visibilitychange', syncPlayback);
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) pause();
    else syncPlayback();
  });
})();
