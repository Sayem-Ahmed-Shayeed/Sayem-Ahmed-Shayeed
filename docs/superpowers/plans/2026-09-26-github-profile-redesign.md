# GitHub Profile README Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Assemble Sayem Ahmed Shayeed's profile README from the cloned reference sections while preserving their existing markup and behavior and personalizing their content.

**Architecture:** The profile repository remains a static GitHub profile README plus the copied SVG assets and GitHub Actions workflows needed to publish the animated project panel and contribution snake. The README links the generated SVGs from the repository's `projects` and `output` branches; hosted image services provide skills icons, the streak card, and the YouTube thumbnail.

**Tech Stack:** Markdown, HTML in GitHub README, SVG/SMIL, GitHub Actions YAML, Python project-card generators, GitHub-hosted workflow artifacts, Skill Icons, GitHub Readme Streak Stats, YouTube thumbnail.

## Global Constraints

- Keep each reference section's markup and behavior intact; change only profile-specific content, usernames, project data, URLs, icon IDs, and required visual values.
- The README order is hero, projects, song, skills and tools, streak and stats, contribution snake.
- Use Sayem's details from `https://sayem-ahmed-shayeed.vercel.app` and the song URL `https://www.youtube.com/watch?v=MoLD4vb0zvQ`.
- The contribution snake remains animated but is not a playable game; adding a playable game would require new application code outside this content-only design.
- GitHub README content does not run custom JavaScript or embedded audio/video players; link the song card to YouTube.
- Do not add or run tests unless requested; use a final content and link audit only.

---

## File Structure

- `README.md` — ordered profile sections and references to local and generated images.
- `readmefile/dark.svg`, `readmefile/light.svg` — the terminal hero's dark/light variants copied from the first profile template and personalized.
- `projects.json` — curated data for the four featured project cards.
- `logos/` — omit optional project logos so the existing generator uses its initials fallback.
- `.github/scripts/fetch_data.py` — copied unchanged from the `arifhaxn` reference to add live GitHub repository data.
- `.github/scripts/generate_projects.py` — copied unchanged from the `arifhaxn` reference to render animated project cards.
- `.github/workflows/projects.yml` — copied unchanged from the `arifhaxn` reference to update the project panel.
- `.github/workflows/snake.yml` — copied unchanged from the `Douglas-Strey` reference to publish light/dark contribution-snake SVGs.

## Tasks

### Task 1: Add the personalized hero and static README sections

**Files:**
- Create: `README.md`
- Create: `readmefile/dark.svg`
- Create: `readmefile/light.svg`

**Interfaces:**
- Produces the opening hero image at `readmefile/dark.svg` and `readmefile/light.svg` for the README `<picture>` element.
- The README uses `Sayem-Ahmed-Shayeed` as the GitHub username and the exact user-provided YouTube video URL.

- [ ] Copy `cloning/readmefile/dark.svg` to `profile/readmefile/dark.svg` and `cloning/readmefile/light.svg` to `profile/readmefile/light.svg` without changing their SVG structure or animation elements.
- [ ] Replace the template identity, location, portfolio, email, social links, focus line, and skill pills in both SVGs with Sayem's portfolio details: Sayem Ahmed Shayeed; Research Assistant at DeepNetLab; Flutter Developer and CSE Student; Sylhet, Bangladesh; `https://sayem-ahmed-shayeed.vercel.app`; `shayeedahmed2@gmail.com`; GitHub, LinkedIn, and Google Scholar; machine learning, computer vision, explainable AI, multimodal AI, Flutter, and Dart.
- [ ] In `README.md`, copy the hero `<picture>` pattern from `cloning/README.md` and point it at the local dark/light SVGs.
- [ ] Add a Projects section placeholder that loads `https://raw.githubusercontent.com/Sayem-Ahmed-Shayeed/Sayem-Ahmed-Shayeed/projects/projects.svg`; Task 2 supplies this generated asset.
- [ ] Add a YouTube song card using the cloned DenverCoder1 video-card anchor/image pattern, replacing its video ID and title with metadata for `MoLD4vb0zvQ`; link the card to `https://www.youtube.com/watch?v=MoLD4vb0zvQ`.
- [ ] Add the Skill Icons image pattern from `cloning/awesome-github-readme-profile/README.md`, using Sayem's portfolio skills: Python, C, C++, Java, Dart, Flutter, Supabase, Firebase, MySQL, and Android Studio.
- [ ] Add the DenverCoder1 streak-card URL pattern with username `Sayem-Ahmed-Shayeed`, preserving the reference theme and query parameters.
- [ ] Keep the final README order as hero, projects, song, skills and tools, streak and stats, contribution snake. Task 3 supplies the snake image.

### Task 2: Add the animated project-list generator

**Files:**
- Create: `projects.json`
- Create: `.github/scripts/fetch_data.py`
- Create: `.github/scripts/generate_projects.py`
- Create: `.github/workflows/projects.yml`
- Modify: `README.md`

**Interfaces:**
- The workflow reads `projects.json`, enriches the repo entries with live GitHub data, and publishes `projects.svg` to branch `projects`.
- The README project image URL is `https://raw.githubusercontent.com/Sayem-Ahmed-Shayeed/Sayem-Ahmed-Shayeed/projects/projects.svg`.

- [ ] Copy `cloning/arifhaxn/.github/scripts/fetch_data.py`, `cloning/arifhaxn/.github/scripts/generate_projects.py`, and `cloning/arifhaxn/.github/workflows/projects.yml` to the matching paths in `profile/` without changing their code.
- [ ] Create `projects.json` in the schema from `cloning/arifhaxn/projects.json` with these four entries, their exact repository URLs, concise portfolio summaries, and tags; omit `logo` so the unchanged generator draws its monogram fallback:
  - `SoundFlow`, repo `Sayem-Ahmed-Shayeed/SoundFlow`, description `Local desktop dictation with faster-whisper and optional AI transcript polish.`, tags `Python`, `Faster Whisper`, `Gemini`.
  - `UniNest`, repo `Sayem-Ahmed-Shayeed/UniNest`, description `Student companion for routines, results, resources, notes, and campus information.`, tags `Flutter`, `Dart`.
  - `Digital Delta`, repo `Sayem-Ahmed-Shayeed/hackathon_project`, description `Offline-first disaster response with peer communication, route intelligence, and logistics.`, tags `C++`, `Dart`, `Offline-first`.
  - `Investify`, repo `Sayem-Ahmed-Shayeed/Investify`, description `Mobile pitch and discovery platform connecting founders with investors.`, tags `Flutter`, `Dart`, `OneSignal`.
- [ ] Preserve the generator's animated card entrance, pulsing activity dot, logo float, cursor, and language-donut animations.
- [ ] Confirm the copied workflow publishes `projects.svg` to the `projects` branch and uses the built-in `GITHUB_TOKEN`; keep its trigger and behavior unchanged.
- [ ] Keep the Task 1 README project image pointed at that published SVG.

### Task 3: Add the animated contribution snake

**Files:**
- Create: `.github/workflows/snake.yml`
- Modify: `README.md`

**Interfaces:**
- The workflow publishes `snake-dark.svg` and `snake-light.svg` to branch `output`.
- The README loads those exact names from `https://raw.githubusercontent.com/Sayem-Ahmed-Shayeed/Sayem-Ahmed-Shayeed/output/`.

- [ ] Copy `cloning/Douglas-Strey/.github/workflows/cobrinha.yml` to `profile/.github/workflows/snake.yml` without changing the workflow logic or output palette.
- [ ] Add the Douglas-Strey `<picture>` pattern at the end of `README.md`, changing only the image host path and accessible alt text to identify Sayem's contribution graph.
- [ ] Ensure the dark source points to `snake-dark.svg` and the fallback light source points to `snake-light.svg` on the `output` branch.

### Task 4: Audit profile-specific content and workflow references

**Files:**
- Review: `README.md`
- Review: `readmefile/dark.svg`
- Review: `readmefile/light.svg`
- Review: `projects.json`
- Review: `.github/scripts/fetch_data.py`
- Review: `.github/scripts/generate_projects.py`
- Review: `.github/workflows/projects.yml`
- Review: `.github/workflows/snake.yml`

**Interfaces:**
- All README image URLs, project repository links, and workflow output filenames agree.

- [ ] Search the profile files for the template usernames `Mahyudeen`, `DenverCoder1`, `arifhaxn`, `Douglas-Strey`, and `zyh3699`; remove any occurrences from rendered profile content and personalized links.
- [ ] Search the profile files for the song video ID `MoLD4vb0zvQ` and verify the card link and thumbnail use that ID.
- [ ] Verify the README section order and that project/snake image URLs match their workflow output branch and filenames.
- [ ] Review the diff for accidental changes to copied workflow or generator logic; do not run tests or workflow jobs unless requested.
