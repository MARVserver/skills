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

## OpenAI Agents SDK

The same reviewed skill catalog can be mounted in the OpenAI Agents SDK without publisher-owned hosted Skill IDs. The included runner packages the committed skills as inline Skill bundles and uses an OpenAI-hosted shell container with network access disabled by default.

```bash
python -m pip install -r requirements-agent-sdk.txt
export OPENAI_API_KEY="..."
python examples/agents_sdk_marketplace.py \
  "Review my production Paper plugin architecture and deployment plan."
```

To restrict the agent to a smaller reviewed surface:

```bash
python examples/agents_sdk_marketplace.py \
  --skill minecraft-plugin-development \
  --skill minecraft-plugin-security \
  "Review this plugin design."
```

See [`AGENTS_SDK.md`](AGENTS_SDK.md) for architecture, usage, hosted Skill IDs, and the security boundary.

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
AGENTS_SDK.md
INSTALL.md
requirements-agent-sdk.txt
examples/
└── agents_sdk_marketplace.py
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

## Safety model

The skills favor version-aware compatibility checks, least privilege, backup and rollback before risky changes, evidence-first debugging, player-data minimization, and explicit verification after operational changes.
