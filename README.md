# MARV Server Engineering for Minecraft

A production-oriented OpenAI/Codex plugin from MARVserver for engineering and operating Minecraft servers.

> **NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.**

The plugin is currently **skills-only**. It bundles 31 domain skills plus an `index` router and does not require a MARVserver-operated MCP server, RCON endpoint, hosting panel, database, telemetry backend, or other external integration.

## Install from the public repository

Codex can add a GitHub `owner/repo` directly as a plugin marketplace source. With a current Codex CLI:

```bash
codex plugin marketplace add MARVserver/skills
codex plugin add marv-server-engineering@marvserver
codex plugin list
```

Start a new Codex thread after installation so the newly installed skills are picked up cleanly.

The repository marketplace entry is:

```text
marv-server-engineering@marvserver
```

## Public policy and support

- [Privacy Policy](PRIVACY.md)
- [Support](SUPPORT.md)
- [Terms of Service](https://marvgame.com/en-US/terms-of-service)
- [Publisher website](https://marvgame.com)
- [GitHub Issues](https://github.com/MARVserver/skills/issues)

Version `0.2.0` is skills-only. Installing or invoking it does not by itself send prompts, files, conversations, server credentials, player data, or execution telemetry to a MARVserver-operated Plugin backend because no such backend is bundled.

## Plugin source

```text
.agents/plugins/marketplace.json
PRIVACY.md
SUPPORT.md
plugins/
└── marv-server-engineering/
    ├── .codex-plugin/plugin.json
    ├── NOTICE.md
    ├── README.md
    ├── assets/README.md
    ├── submission/
    │   ├── LISTING.md
    │   ├── RELEASE_NOTES.md
    │   ├── SUBMISSION_CHECKLIST.md
    │   └── TEST_CASES.md
    └── skills/
        ├── index/SKILL.md
        └── <domain-skill>/SKILL.md
```

## Coverage

### Development and engineering

- `minecraft-plugin-development`
- `minecraft-plugin-architecture`
- `minecraft-plugin-testing-debugging`
- `minecraft-plugin-performance`
- `minecraft-plugin-data-integrations`
- `minecraft-plugin-security`
- `minecraft-plugin-release-compatibility`
- `minecraft-mod-development`
- `minecraft-datapack-resourcepack-automation`

### Server platform and gameplay

- `minecraft-server-configuration`
- `minecraft-network-proxy`
- `minecraft-permissions-access-control`
- `minecraft-world-content-management`
- `minecraft-gameplay-economy`
- `minecraft-anti-cheat-abuse-prevention`
- `minecraft-security-privacy`

### Reliability and DevOps

- `minecraft-server-operations`
- `minecraft-deployments`
- `minecraft-observability`
- `minecraft-backup-recovery`
- `minecraft-performance`
- `minecraft-incident-response`

### LiveOps and server management

- `minecraft-moderation`
- `minecraft-community-management`
- `minecraft-staff-operations`
- `minecraft-player-support`
- `minecraft-events-liveops`
- `minecraft-capacity-cost-planning`
- `minecraft-documentation-change-management`
- `minecraft-store-commerce`
- `minecraft-analytics-product-ops`

## Distribution status

### Codex

The plugin is distributable directly from this public GitHub repository through the repository marketplace shown above.

### ChatGPT Plugin Directory

OpenAI's current Plugin model can contain skills without requiring an app. This repository contains listing copy, starter prompts, release notes, and QA cases for a future public-directory handoff. Publishing to the global Plugin Directory is a separate OpenAI-side publishing/submission action; making this GitHub repository public does not automatically create a global Plugin Directory listing.

`submission/TEST_CASES.md` contains five positive and three negative QA cases. That count mirrors OpenAI's documented ChatGPT **app** submission review format and is useful for regression testing, but this repository does not claim that the same count is a mandatory requirement for every skills-only Plugin submission.

See [`submission/SUBMISSION_CHECKLIST.md`](plugins/marv-server-engineering/submission/SUBMISSION_CHECKLIST.md) for the remaining handoff items.

## Safety model

The skills use version-aware compatibility checks, least privilege, backup/rollback before risky changes, evidence-first incident handling, player-data minimization, and explicit separation between advice and actions that require actual runtime tools and authorization.

## Future app/MCP layer

Optional integrations can later add RCON, Pterodactyl or other panels, GitHub, Discord, Prometheus/Grafana, databases, object storage, and deployment systems without changing the domain skill model. If a MARVserver-operated backend is added, update the Privacy Policy and listing before release.
