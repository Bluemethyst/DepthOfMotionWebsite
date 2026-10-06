/* Navigation is progressively enhanced: all links stay visible without JS. */
(() => {
  const toggle = document.querySelector('.nav-toggle');
  const navigation = document.querySelector('#site-navigation');
  if (!toggle || !navigation) return;
  document.documentElement.classList.add('js');
  const label = toggle.querySelector('[data-menu-label]');
  const icon = toggle.querySelector('[data-menu-icon]');

  function setOpen(open, returnFocus = false) {
    toggle.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
    label.textContent = open ? 'Close' : 'Menu';
    icon.textContent = open ? '−' : '+';
    if (returnFocus) toggle.focus();
  }

  toggle.addEventListener('click', () => {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false, true);
    }
  });
  document.addEventListener('click', (event) => {
    if (!event.target.closest('.site-header')) setOpen(false);
  });
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });
  const desktop = window.matchMedia('(min-width: 1151px)');
  desktop.addEventListener('change', () => setOpen(false));
})();
