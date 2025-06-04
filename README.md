 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10206799.svg)](https://doi.org/10.5281/zenodo.10206799)
 ![2024 Cover](./media/2024_AU-SSI_Probability_Slides.png)
 ![2023 Cover](./media/2023_AU-SSI_Probability_Slides.png)
 ![2022 Cover](./media/2022_AU-SSI_Probability_Slides.png)

 # Summer Science Institute at Auburn — Probability Module

 A collection of slides, code examples, and resources for the “Probability” topic presented by Le Chen at Auburn University's Summer Science Institute (SSI), 2022–2024.

 ## Table of Contents

 1. [What’s in this repo?](#whats-in-this-repo)
 2. [Repository Structure](#repository-structure)
 3. [Building the Slides](#building-the-slides)
 4. [Per-Year Materials](#per-year-materials)
 5. [Contributing](#contributing)
 6. [License](#license)

 ## What’s in this repo?

 - Slide decks (PDF & TeX source) for each year’s presentation.
 - Python code examples and simulation scripts.
 - Data files, figures, and photos used in demonstrations.
 - Documentation per year (Year_2022.md, Year_2023.md, Year_2024.md).

 ## Repository Structure

 ```
 .
 ├── 2022_slides/       # TeX source, compiled PDF, code, and figures for 2022
 ├── 2023_slides/       # TeX source, compiled PDF, code, figures, and photos for 2023
 ├── media/             # Covers and images for each year
 ├── Year_2022.md       # Overview, attendees, and instructions for 2022
 ├── Year_2023.md       # Overview, talk abstract, and report for 2023
 ├── Year_2024.md       # Overview and slide link for 2024
 ├── LICENSE            # CC-BY-SA-4.0 license
 └── README.md          # You are here
 ```

 ## Building the Slides

 **Dependencies:**
 - TeX Live (including LaTeX, Beamer, TikZ, etc.)
 - `latexmk` (recommended) or `pdflatex`

 **Compile commands:**
 ```bash
 # From the repository root, build each deck:
 cd 2022_slides
 latexmk -pdf 2022_AU-SSI_Invitation_Probability_Le.tex

 cd ../2023_slides
 latexmk -pdf 2023_AU-SSI_Probability_Le.tex

 # 2024 slides are hosted online; no local TeX source
 ```

 ## Per-Year Materials

 ### Year 2022
 - **Slides:** `2022_slides/2022_AU-SSI_Invitation_Probability_Le.pdf`
 - **Source:** TeX files and style in `2022_slides/`
 - **Code & data:** `2022_slides/codes/`
 - **Figures:** `2022_slides/figs/`
 - **Overview:** [Year_2022.md](Year_2022.md)

 ### Year 2023
 - **Slides:** `2023_slides/2023_AU-SSI_Probability_Le.pdf`
 - **Source:** TeX files in `2023_slides/`
 - **Code:** `2023_slides/codes/`
 - **Figures:** `2023_slides/figs/`
 - **Photos:** `2023_slides/photos/`
 - **Report:** `2023_slides/2023_SSI_Program_Report_Final.pdf`
 - **Overview:** [Year_2023.md](Year_2023.md)

 ### Year 2024
 - **Slides:** Hosted online at [webhome.auburn.edu/~lzc0090/AU-SSI_2024](http://webhome.auburn.edu/~lzc0090/AU-SSI_2024/#/)
 - **Overview:** [Year_2024.md](Year_2024.md)

 ## Contributing

 Contributions (typo fixes, code enhancements, new demos) are welcome! Please see `CONTRIBUTING.md` for guidelines.

 ## License

 This repository is licensed under [CC-BY-SA-4.0](LICENSE). See the LICENSE file for full details.