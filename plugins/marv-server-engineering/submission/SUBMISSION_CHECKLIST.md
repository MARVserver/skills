# Public Plugin Directory submission checklist

This checklist separates repository work from publisher/account actions that cannot be safely inferred or completed from source code alone.

## Package — complete

- [x] Skills-only plugin manifest exists.
- [x] Plugin ID is `marv-server-engineering`.
- [x] Public name does not use `Minecraft` as the first/dominant brand element.
- [x] Non-affiliation disclaimer is included in manifest/listing/repository materials.
- [x] 31 domain skills plus one router skill are packaged under `./skills/`.
- [x] Three starter prompts are prepared.
- [x] At least five positive review test cases are prepared.
- [x] At least three negative review test cases are prepared.
- [x] Initial release notes are prepared.
- [x] Website, publisher email, support URL, terms URL, and privacy URL are documented.
- [x] Canonical Privacy Policy is present at repository root as `PRIVACY.md`.
- [x] Plugin-specific support guidance is present at repository root as `SUPPORT.md`.
- [x] No MARVserver-operated MCP/app backend is required for version 0.2.0.

## Public-source gate

- [ ] Repository visibility is Public.
- [ ] Confirm https://github.com/MARVserver/skills is readable while signed out.
- [ ] Confirm https://github.com/MARVserver/skills/blob/main/PRIVACY.md is readable while signed out after this PR is merged.
- [ ] Confirm https://github.com/MARVserver/skills/issues is available as the public support page.

## Publisher-controlled items

- [ ] Supply an original MARVserver-owned square logo for the listing; do not use Minecraft/Mojang/Microsoft brand assets.
- [ ] Review the final Privacy Policy and Terms URLs as publisher policy before submission.
- [ ] Select countries/regions based on actual support and legal readiness.

## OpenAI account / submission

- [ ] Confirm the submitting OpenAI account/workspace has access to the current Plugin publishing/submission flow.
- [ ] Create the public submission as **Skills only** where that option is available.
- [ ] Use the listing copy and starter prompts from `submission/LISTING.md`.
- [ ] Run and record the positive/negative cases from `submission/TEST_CASES.md` against the exact release bundle.
- [ ] Supply availability and release notes.
- [ ] Submit for review/publishing through the current OpenAI Plugin workflow.

## Pre-submit quality gate

- [ ] Recheck every public URL from an unauthenticated browser.
- [ ] Confirm no credentials, private hostnames, production IPs, player PII, or confidential internal material are included.
- [ ] Confirm all listing claims match the current skills-only capabilities.
- [ ] Confirm the Privacy Policy still matches the actual data flow; update it before any future MARVserver-operated app/MCP/telemetry backend is enabled.
- [ ] Confirm the Minecraft non-affiliation notice remains prominent.
