# Release notes

## 0.2.0 — public distribution candidate

- Package the MARVserver Minecraft engineering and operations catalog as a skills-only OpenAI/Codex plugin.
- Provide 31 specialist skills plus an `index` routing skill.
- Cover plugin/mod development, platform configuration, proxy/networking, permissions/security, world/economy systems, SRE/DevOps, moderation, community/staff/support operations, LiveOps, commerce, analytics, and capacity planning.
- Publish the repository for direct Codex marketplace installation.
- Publish canonical `PRIVACY.md` and `SUPPORT.md` documents and expose public support through GitHub Issues.
- Add three starter prompts and positive/negative QA cases for release testing.
- Rename the public product to `MARV Server Engineering for Minecraft` and add an explicit Mojang/Microsoft non-affiliation disclaimer.
- Keep external runtime integrations out of this release; no MCP server or MARVserver backend is required.
- Add automated package validation for the manifest, marketplace, 31 domain skills plus router, public policy URLs, and branding disclaimer.
- Add tag-driven GitHub Release automation that produces a versioned ZIP and SHA-256 checksum.

### Remaining directory-publishing items

- Supply a publisher-approved, MARVserver-owned high-resolution square listing logo. The existing website favicon is only 16×16 pixels and is not used as the primary listing logo.
- Complete any publisher/account verification and directory-submission steps required by the OpenAI surface available to the submitting account.
- Select final availability countries/regions where required by the publishing flow.

### Distribution

Public Codex installation:

```bash
codex plugin marketplace add MARVserver/skills
codex plugin add marv-server-engineering@marvserver
```
