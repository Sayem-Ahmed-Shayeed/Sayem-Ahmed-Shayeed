# GitHub Profile README Redesign

## Goal

Build Sayem Ahmed Shayeed's profile README by adapting the supplied GitHub profile references. Preserve each reference section's markup and behavior; replace only profile-specific content, links, and values wherever possible.

## Audience and tone

Visitors to Sayem's GitHub profile, especially research collaborators, scholarship committees, and software collaborators. The profile should feel personal, technical, and easy to scan, using the dark terminal aesthetic from the hero reference and the visual styles shown in the supplied section screenshots.

## README order and content

1. **Hero:** Use the supplied terminal-window hero composition. Replace the template identity and biography with Sayem's name, role, focus, location, portfolio portrait, and public contact/social links from `sayem-ahmed-shayeed.vercel.app`.
2. **Projects:** Use the cloned `arifhaxn/arifhaxn` project-list card treatment and its existing data structure. Populate it with Sayem's featured projects from his portfolio and link each card to the corresponding repository.
3. **Song:** Add a clickable YouTube song card using the exact URL supplied by Sayem: `https://www.youtube.com/watch?v=MoLD4vb0zvQ`. The card opens YouTube; GitHub README content does not support an embedded player with playback.
4. **Skills and tools:** Use the existing Skill Icons image pattern and select skills listed on Sayem's portfolio.
5. **Streak and stats:** Reuse the DenverCoder1 streak card pattern with Sayem's username and the profile's dark palette.
6. **Contribution snake:** Reuse the Douglas-Strey contribution-snake pattern, configured for Sayem's account and both color schemes. Preserve its animation behavior.

## Implementation constraints

- Keep the source section markup and behavior intact. Change content, usernames, project data, URLs, icon IDs, and visual values required to personalize the sections.
- Do not introduce custom interactions into the README. GitHub renders README HTML as restricted content and does not run custom JavaScript or embedded audio/video players.
- The contribution snake remains the reference's animated contribution visualization. A playable Snake game would require a separate application and new code, which is outside this content-only design.
- Keep all profile assets in the profile repository and use theme-aware image variants where the references already support them.
- The workspace clone is named `profile/`; the GitHub repository is currently empty.

## Data sources

- Portfolio website: `https://sayem-ahmed-shayeed.vercel.app`
- User-provided song link: `https://www.youtube.com/watch?v=MoLD4vb0zvQ`
- Cloned references: `cloning/` in the workspace (Skill Icons, DenverCoder1, arifhaxn, Douglas-Strey, and the previously cloned hero template).

## Acceptance criteria

- The README sections appear in the order above.
- The hero, project cards, skill icons, streak, and snake contain Sayem's details, not template authors' details.
- Project cards and social/contact controls point to Sayem's own destinations.
- The song card links to the exact video supplied by Sayem.
- Light/dark image alternatives and contribution-snake animation follow the cloned references.
- No new game or other custom README interaction is added under the content-only constraint.
