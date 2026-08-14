# Public Plugin distribution checklist

This checklist separates completed public-source work from publisher/account actions that remain outside the repository.

## Package — complete

- [x] Skills-only plugin manifest exists.
- [x] Plugin ID is `marv-server-engineering`.
- [x] Public name does not use `Minecraft` as the first/dominant brand element.
- [x] Non-affiliation disclaimer is included in manifest/listing/repository materials.
- [x] 31 domain skills plus one router skill are packaged under `./skills/`.
- [x] Three starter prompts are prepared.
- [x] Five positive and three negative QA cases are prepared.
- [x] Initial release notes are prepared.
- [x] Website, publisher email, support URL, terms URL, and privacy URL are documented.
- [x] Canonical Privacy Policy is present at repository root as `PRIVACY.md`.
- [x] Plugin-specific support guidance is present at repository root as `SUPPORT.md`.
- [x] No MARVserver-operated MCP/app backend is required for version 0.2.0.

## Public-source gate — complete

- [x] Repository visibility is Public.
- [x] Public repository source is available at `https://github.com/MARVserver/skills`.
- [x] Canonical privacy source exists at `https://github.com/MARVserver/skills/blob/main/PRIVACY.md`.
- [x] GitHub Issues endpoint is enabled for plugin support.
- [x] Public Codex marketplace entry resolves to `marv-server-engineering@marvserver`.

## Codex distribution — complete

Install from the public repository marketplace:

```bash
codex plugin marketplace add MARVserver/skills
codex plugin add marv-server-engineering@marvserver
```

Use a new thread after installation.

## Publisher-controlled items

- [ ] Supply an original MARVserver-owned square logo for any directory listing that requires one; do not use Minecraft/Mojang/Microsoft brand assets.
- [ ] Publisher-review the final Privacy Policy and Terms URLs before any global directory submission.
- [ ] Select countries/regions if the OpenAI publishing flow requests availability settings.

## OpenAI global Plugin Directory

- [ ] Confirm the submitting account/workspace has access to the current Plugin publishing/submission flow.
- [ ] Use the listing copy and starter prompts from `submission/LISTING.md`.
- [ ] Run the QA cases from `submission/TEST_CASES.md` against the exact release bundle.
- [ ] Supply any additional fields requested by the current OpenAI publishing UI.
- [ ] Submit/publish through the OpenAI workflow available to the publisher account.

The five-positive/three-negative case count is maintained as a useful review/regression format. OpenAI explicitly documents that exact count for ChatGPT **app/MCP** submission artifacts; do not represent it as a confirmed mandatory rule for every skills-only Plugin unless the current publishing UI or official documentation says so.

## Pre-publish quality gate

- [ ] Recheck every public URL from an unauthenticated browser immediately before submission.
- [ ] Confirm no credentials, private hostnames, production IPs, player PII, or confidential internal material are included.
- [ ] Confirm all listing claims match the current skills-only capabilities.
- [ ] Confirm the Privacy Policy still matches the actual data flow; update it before any future MARVserver-operated app/MCP/telemetry backend is enabled.
- [ ] Confirm the Minecraft non-affiliation notice remains prominent.
