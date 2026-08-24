# MARVserver Minecraft Skills

A production-oriented Minecraft server engineering and operations skill pack maintained by MARVserver.

> **NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.**

It contains 31 specialist skills plus an `index` router. The pack is skills-only: no MARVserver account, API key, MCP server, RCON endpoint, database, or hosted backend is required.

## Install

Copy and paste one line:

```bash
codex plugin marketplace add MARVserver/skills && codex plugin add marv-server-engineering@marvserver
```

Then start a new Codex thread.

If the marketplace is already registered, install/reinstall with:

```bash
codex plugin add marv-server-engineering@marvserver
```

Verify with:

```bash
codex plugin list
```

The installed entry is:

```text
marv-server-engineering@marvserver
```

See [`INSTALL.md`](INSTALL.md) for the short installation guide.

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

## Repository structure

```text
.agents/plugins/marketplace.json
INSTALL.md
plugins/
└── marv-server-engineering/
    ├── .codex-plugin/plugin.json
    ├── NOTICE.md
    ├── README.md
    └── skills/
        ├── index/SKILL.md
        └── <domain-skill>/SKILL.md
scripts/
└── validate_plugin.py
```

## Validation

Run locally with:

```bash
python3 scripts/validate_plugin.py
```

The same validation runs automatically on pull requests and pushes to `main`.

## Community

- Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing or implementing a substantial change.
- Use [GitHub Discussions](https://github.com/MARVserver/skills/discussions) for questions, troubleshooting, ideas, and early design discussion.
- Use the structured [Issue forms](https://github.com/MARVserver/skills/issues/new/choose) for actionable bugs and feature work.
- See [`SUPPORT.md`](SUPPORT.md) for routing and support boundaries.
- See [`SECURITY.md`](SECURITY.md) before reporting a vulnerability.
- The initial wiki content is maintained under [`docs/wiki/`](docs/wiki/Home.md) and can be published to the GitHub Wiki when the repository Wiki feature is enabled.
- Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Safety model

The skills favor version-aware compatibility checks, least privilege, backup and rollback before risky changes, evidence-first debugging, player-data minimization, and explicit verification after operational changes.
