 # TODO
 This file collects suggested improvements for the repository.

 ## 1. Rename and polish top-level README
 - Rename `readme.md` to `README.md`.
 - Add a clear "What's in this repo?" section or table of contents with links to each year's materials.
 - Include build instructions for `.tex` slide decks (dependencies, build commands).
 - Link to per-year folders and explain their contents (slides, code, data, photos).

 ## 2. Organize directories consistently
 - Group by year: `2022/`, `2023/`, `2024/`.
 - Within each year folder, use subfolders like `slides/`, `code/`, `data/`, `photos/`.
 - Avoid parallel hierarchies like `2022_slides`, `2023_slides`.

 ## 3. Manage large binaries
 - Move high-res figures to Git LFS or host externally (Zenodo, release assets).
 - Compress images where possible (optimize PNG, convert to SVG).

 ## 4. Add build infrastructure & CI
 - Provide a `Makefile` or `build.sh` to compile all slide decks.
 - Add a GitHub Actions workflow to build PDFs and run Python lint/tests on each PR.

 ## 5. Polish code examples
 - Add `requirements.txt` or `environment.yml` listing Python dependencies.
 - In each `code/` folder, add a small README describing each script and usage examples.
 - Use `argparse`, context managers, and add minimal smoke tests.

 ## 6. Community files
 - Add `CONTRIBUTING.md` with guidelines for contributions.
 - Add `CODE_OF_CONDUCT.md` (e.g. Contributor Covenant).
 - Provide issue/PR templates under `.github/`.

 ## 7. Improve metadata & badges
 - Add a CC-BY-SA badge (e.g. shields.io).
 - Display build status badge for LaTeX compilation and Python lint/tests.
 - Optimize the GitHub repo description.

 ## 8. Versioning & changelog
 - Add `CHANGELOG.md` to track what's new each year.

 ## 9. GitHub Pages (optional)
 - Publish slide decks or HTML versions via GitHub Pages for in-browser viewing.

 ## 10. Cleanup & housekeeping
 - Add a `.gitignore` for `__pycache__/`, LaTeX build artifacts, editor swap files.
 - Remove stray backups or temporary files.
 - Enable branch protection and require CI passing before merging.