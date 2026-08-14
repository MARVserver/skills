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
- [x] Website, publisher email, support-page candidate, and terms URL are documented.
- [x] No MARVserver-operated MCP/app backend is required for version 0.2.0.

## Publisher-controlled blockers — required before public submission

- [ ] Approve a dedicated plugin privacy policy after confirming real data recipients, retention periods, user-control process, and security practices.
- [ ] Publish that policy at a stable public HTTPS URL and add it to the OpenAI listing/manifest.
- [ ] Supply an original MARVserver-owned square logo and upload it for the listing; do not use Minecraft/Mojang/Microsoft brand assets.
- [ ] Verify that the public support URL works and exposes an acceptable contact path; keep `marvsystem@gmail.com` as the direct publisher contact.
- [ ] Select countries/regions based on actual support and legal readiness.

## OpenAI Platform account — required before review

- [ ] Complete the developer/business identity verification required by OpenAI for public publishing.
- [ ] Ensure the submitting account has the required Apps Management write permission.
- [ ] Create a new plugin submission and choose **Skills only**.
- [ ] Upload the final skill bundle and listing data.
- [ ] Enter the starter prompts, positive/negative review cases, availability, and release notes.
- [ ] Submit for OpenAI review.
- [ ] After approval, perform the separate publish action when the portal makes it available.

## Pre-submit quality gate

- [ ] Run all positive and negative test cases against the exact bundle being submitted.
- [ ] Recheck every public URL from an unauthenticated browser.
- [ ] Confirm no credentials, private hostnames, production IPs, player PII, or confidential internal material are included.
- [ ] Confirm all claims in the listing match the current skills-only capabilities.
- [ ] Confirm the privacy policy and retention commitments match real operations.
- [ ] Confirm the Minecraft non-affiliation notice remains prominent.
