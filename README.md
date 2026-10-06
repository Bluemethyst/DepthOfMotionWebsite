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
- Both biography files have identical text. Relevant passages are reused on Home, Adult Dance, Women’s Movement and Creative Work because separate descriptions were not supplied. The complete biography appears on About. One joined-name spacing error was corrected; no new biography claims were added.
- The supplied flyer resolves the earlier email typo: general enquiries now use **connect@depthofmotion.nz**. Women’s movement retains **alive@depthofmotion.nz** from the original brief.
- Exact term start/end dates, actual film files and further project descriptions were not supplied, so these are not invented or displayed. The empty logo folders are represented by a text wordmark.

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

Enquiries use phone/email links. The downloadable enrolment PDF is the original printable form; there is no online booking, data collection, payment processing or password-protected gallery.
