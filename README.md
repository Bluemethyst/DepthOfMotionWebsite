# Depth of Motion

Six static pages for Alexandra Tylee’s dance and movement practice in Mohua / Golden Bay. Vanilla HTML, shared CSS and a small mobile-navigation script. No build step or runtime dependencies.

## Preview

Open `index.html` directly, or run this from the project folder:

```sh
python scripts/serve.py
```

Visit **http://127.0.0.1:4173/DepthOfMotionWebsite/**. This also tests repository-subdirectory paths. Press Ctrl+C to stop; use `--port 8080` if necessary.

## Content and images

All generated marketing copy, concept photographs, sample projects, portrait placeholders and logo artwork have been removed. The website uses the supplied photographs, biography, class flyer and enrolment form. The original source folder has not been changed.

Edit content directly in the six HTML files. Shared header/footer markup is included in each file so navigation works without JavaScript; update all six copies for shared changes. Colours and layouts are in `assets/css/styles.css`; navigation behaviour is in `assets/js/main.js`.

Photographs are in `assets/images/`, and the unchanged class flyer and enrolment PDF are in `assets/downloads/`. [The asset guide](assets/README.md) maps filenames to the supplied sources and explains the copy choices. [The source map](assets/source-map.json) records image dimensions and alt text. Update these attributes and any credits when replacing photographs. Keep links relative without a leading `/`.

The stable page filenames and section IDs can later be mapped to Pages CMS content and templates. No CMS or build system is installed.

## Source details to resolve

- The flyer specifies **ages 9–15** for Intermediate & Senior Ballet; the Term 4 enrolment form specifies **9–14** for Intermediate Ballet. The website currently uses the term-specific form’s range and displays a note beside the timetable.
- The flyer’s “Choreographic Lab” and form’s “Choreographic Contemporary” labels are retained in their respective timetable and fees sections.
- Both original biography files have identical text. The complete biography appears on About, with relevant excerpts on Home and Creative Work. Adult Dance and Women’s Movement now use the separate descriptions supplied in `Re__Files_`. Every paragraph from both updated Word documents is included.
- The new flyer’s filename says contemporary, but its heading says adult ballet. The adult class details follow the printed flyer: Tuesday 5:40–7:00 pm, five-week block starting 7 October, $80 per block or $20 per session. The flyer does not give a year; none is inferred.
- Women’s sessions follow the updated description: fortnightly in the rhythm of the waxing and waning moon, 1.5 hours, $20–30 per session, at Kōtinga Hall. No dates or weekly time are inferred.
- The supplied flyer resolves the earlier email typo: general enquiries now use **connect@depthofmotion.nz**. Women’s movement retains **alive@depthofmotion.nz** from the original brief.
- Exact term start/end dates or a year for the adult block, actual film files and further project descriptions were not supplied, so these are not invented or displayed. The empty logo folders are represented by a text wordmark.

## GitHub Pages

No repository URL has been supplied and the site has not been published.

1. Add the six HTML files, `assets/`, `.nojekyll`, `.gitignore`, `README.md` and `scripts/` to the intended repository. Exclude the ignored `artifacts/` directory.
2. Push to the publishing branch, usually `main`.
3. In **Settings → Pages**, choose **Deploy from a branch**, that branch and **/(root)**, then save.
4. Use the deployment URL shown by GitHub after it finishes. All website paths support a repository subdirectory.

See [GitHub’s publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Verification

```sh
python scripts/check_site.py
node --check assets/js/main.js
```

The checker verifies the six pages, links and anchors, image assets, navigation states and unique metadata. Browser QA checks responsive widths, loading, accessibility, menu behaviour, keyboard use, reduced motion and navigation without JavaScript. Local reports and screenshots are kept in the ignored `artifacts/` folder.

The children’s website fee table shows term fees only. Its photography section has been removed; the original photos remain available in the asset folder. The downloadable enrolment PDF remains the original supplied printable form.

Adult Dance and Women’s Movement have small mailing-list sections. Their links open a prefilled email request to `connect@depthofmotion.nz` and `alive@depthofmotion.nz` respectively. Visitors must send the email to request joining; the site does not automatically subscribe anyone or store their details. A mailing-list service can replace these links later if one is supplied.

Instagram and Facebook links appear in every footer, using the exact customer-supplied profiles. Enquiries use phone/email links. There is no online booking, payment processing or password-protected gallery.

## Creative Work video

Creative Work includes a working native HTML video player and the complete compressed film in `assets/video/creative-movement.mp4` (37.8 MiB). The original 921.2 MiB file remains outside the repository. The player loads the poster first, starts only when the visitor presses play and supports mobile playback and fullscreen.

For the live site, an unlisted YouTube upload is recommended for streaming and quality selection. Upload the original, allow embedding, then replace the video element with a responsive iframe using `https://www.youtube-nocookie.com/embed/VIDEO_ID`, a descriptive title and fullscreen permission. Use the actual video ID; do not publish a placeholder. An unlisted video is accessible to anyone with the link. A custom player controls the interface but still needs a media host. The current compressed MP4 can be hosted as a static GitHub Pages asset; the full original exceeds GitHub’s 100 MiB individual Git file limit.

The local preview server supports MP4 byte ranges so visitors can seek through the film during preview. Browser checks verify that the video is not requested before play, then plays and seeks at both desktop and mobile widths.
