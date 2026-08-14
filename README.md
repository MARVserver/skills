# MARV Server Engineering for Minecraft

A production-oriented OpenAI plugin from MARVserver for engineering and operating Minecraft servers.

> **NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.**

The plugin is currently **skills-only**. It bundles 31 domain skills plus an `index` router and does not require a MARVserver-operated MCP server, RCON endpoint, hosting panel, database, or other external integration.

## Plugin source

```text
.agents/plugins/marketplace.json
plugins/
└── marv-server-engineering/
    ├── .codex-plugin/plugin.json
    ├── NOTICE.md
    ├── README.md
    ├── assets/README.md
    ├── submission/
    │   ├── LISTING.md
    │   ├── PRIVACY_POLICY_DRAFT.md
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

The repository now includes the material needed to prepare a skills-only public Plugin Directory submission: listing copy, three starter prompts, positive/negative review cases, release notes, and a submission checklist.

Two publisher-controlled items intentionally remain outside the code bundle:

1. approve and publish a dedicated privacy policy with real MARVserver retention practices;
2. provide a MARV-owned logo asset for the public listing.

OpenAI developer/business verification and the required Platform permissions must also be completed by the submitting account before public review.

See [`submission/SUBMISSION_CHECKLIST.md`](plugins/marv-server-engineering/submission/SUBMISSION_CHECKLIST.md) for the final handoff.

## Local/repository marketplace

After cloning the repository, the repo-local marketplace identifies the plugin as `marv-server-engineering@marvserver`.

## Safety model

The skills use version-aware compatibility checks, least privilege, backup/rollback before risky changes, evidence-first incident handling, player-data minimization, and explicit separation between advice and actions that require actual runtime tools and authorization.

## Future app/MCP layer

Optional integrations can later add RCON, Pterodactyl or other panels, GitHub, Discord, Prometheus/Grafana, databases, object storage, and deployment systems without changing the domain skill model.
