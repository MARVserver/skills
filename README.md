# MARVserver Minecraft Server Engineering Plugin

An OpenAI plugin bundle for production-oriented Minecraft server engineering and operations.

This repository packages **31 domain skills plus one plugin router skill** covering extension development, server/platform engineering, reliability, security, moderation, staff/player operations, LiveOps, commerce, analytics, and capacity planning.

The bundle is currently **skills-only**: it does not declare an external app or MCP server. That keeps installation independent from any specific hosting panel, RCON endpoint, database, monitoring stack, or provider. External actions can be added later as an app/MCP layer without rewriting the skills.

## OpenAI plugin layout

```text
.agents/plugins/marketplace.json
plugins/
└── minecraft-server-engineering/
    ├── .codex-plugin/
    │   └── plugin.json
    ├── README.md
    └── skills/
        ├── index/
        │   └── SKILL.md
        └── <domain-skill>/
            └── SKILL.md
```

The plugin manifest points to `./skills/`. The repo-level marketplace file declares the plugin as a local team/repository plugin.

> Publishing to the public OpenAI Plugin Directory is a separate distribution/review step. This repository provides the source bundle and local marketplace metadata.

## Development and engineering

| Skill | Use it for |
| --- | --- |
| [`minecraft-plugin-development`](plugins/minecraft-server-engineering/skills/minecraft-plugin-development/SKILL.md) | Commands, events, schedulers, lifecycle, configuration, APIs, and production plugin implementation |
| [`minecraft-plugin-architecture`](plugins/minecraft-server-engineering/skills/minecraft-plugin-architecture/SKILL.md) | Domain/service/platform boundaries, lifecycle ownership, adapters, and maintainable plugin design |
| [`minecraft-plugin-testing-debugging`](plugins/minecraft-server-engineering/skills/minecraft-plugin-testing-debugging/SKILL.md) | Unit/integration tests, isolated server tests, bug reproduction, stack traces, and regression coverage |
| [`minecraft-plugin-performance`](plugins/minecraft-server-engineering/skills/minecraft-plugin-performance/SKILL.md) | Tick-thread load, hot events, allocation, queues, I/O, queries, caching, and plugin profiling |
| [`minecraft-plugin-data-integrations`](plugins/minecraft-server-engineering/skills/minecraft-plugin-data-integrations/SKILL.md) | SQL, embedded databases, caches, HTTP APIs, bots, message systems, and cross-server state |
| [`minecraft-plugin-security`](plugins/minecraft-server-engineering/skills/minecraft-plugin-security/SKILL.md) | Authorization, untrusted input, secrets, SQL/file safety, rate limits, and abuse-resistant plugin code |
| [`minecraft-plugin-release-compatibility`](plugins/minecraft-server-engineering/skills/minecraft-plugin-release-compatibility/SKILL.md) | CI/builds, artifacts, compatibility matrices, migrations, releases, changelogs, and rollback |
| [`minecraft-mod-development`](plugins/minecraft-server-engineering/skills/minecraft-mod-development/SKILL.md) | Loader-aware mod development, side separation, networking, mappings, persistence, and packaging |
| [`minecraft-datapack-resourcepack-automation`](plugins/minecraft-server-engineering/skills/minecraft-datapack-resourcepack-automation/SKILL.md) | Datapacks, resource packs, functions, generated content, validation, performance, and deployment |

## Server platform and gameplay

| Skill | Use it for |
| --- | --- |
| [`minecraft-server-configuration`](plugins/minecraft-server-engineering/skills/minecraft-server-configuration/SKILL.md) | Server/proxy/plugin/mod/JVM/service configuration, diffs, validation, activation, and rollback |
| [`minecraft-network-proxy`](plugins/minecraft-server-engineering/skills/minecraft-network-proxy/SKILL.md) | Proxies, routing, backend isolation, forwarding/authentication, DNS, firewalls, and failover |
| [`minecraft-permissions-access-control`](plugins/minecraft-server-engineering/skills/minecraft-permissions-access-control/SKILL.md) | Permission groups, staff/admin capabilities, console/panel access, service accounts, and audits |
| [`minecraft-world-content-management`](plugins/minecraft-server-engineering/skills/minecraft-world-content-management/SKILL.md) | Worlds, dimensions, resets, pregeneration, maps, migration, regions, and content rollout |
| [`minecraft-gameplay-economy`](plugins/minecraft-server-engineering/skills/minecraft-gameplay-economy/SKILL.md) | Virtual currencies, rewards, shops, progression, sources/sinks, exploit controls, and balance |
| [`minecraft-anti-cheat-abuse-prevention`](plugins/minecraft-server-engineering/skills/minecraft-anti-cheat-abuse-prevention/SKILL.md) | Anti-cheat signals, exploits, duplication, botting, false positives, containment, and evidence |
| [`minecraft-security-privacy`](plugins/minecraft-server-engineering/skills/minecraft-security-privacy/SKILL.md) | Host/service hardening, secrets, patching, audit logs, player-data minimization, and access review |

## Reliability and DevOps

| Skill | Use it for |
| --- | --- |
| [`minecraft-server-operations`](plugins/minecraft-server-engineering/skills/minecraft-server-operations/SKILL.md) | Start/stop/restart, console operations, health checks, routine maintenance, and safe admin work |
| [`minecraft-deployments`](plugins/minecraft-server-engineering/skills/minecraft-deployments/SKILL.md) | Server/proxy/plugin/mod/config/Java rollouts with compatibility checks, staged verification, and rollback |
| [`minecraft-observability`](plugins/minecraft-server-engineering/skills/minecraft-observability/SKILL.md) | TPS/MSPT, JVM, host, disk, network, logs, alert triage, and profiling |
| [`minecraft-backup-recovery`](plugins/minecraft-server-engineering/skills/minecraft-backup-recovery/SKILL.md) | Consistent backups, retention, off-host copies, restore drills, and disaster recovery |
| [`minecraft-performance`](plugins/minecraft-server-engineering/skills/minecraft-performance/SKILL.md) | Server-wide lag diagnosis and evidence-based tuning of chunks, entities, JVM, host, plugins, and mods |
| [`minecraft-incident-response`](plugins/minecraft-server-engineering/skills/minecraft-incident-response/SKILL.md) | Crash loops, corruption, failed deploys, exhaustion, dependency/network incidents, containment, and recovery |

## LiveOps and server management

| Skill | Use it for |
| --- | --- |
| [`minecraft-moderation`](plugins/minecraft-server-engineering/skills/minecraft-moderation/SKILL.md) | Warnings, mutes, bans, evidence review, appeals, proportional enforcement, and moderator quality |
| [`minecraft-community-management`](plugins/minecraft-server-engineering/skills/minecraft-community-management/SKILL.md) | Announcements, feedback loops, onboarding, community channels, roadmap communication, and community health |
| [`minecraft-staff-operations`](plugins/minecraft-server-engineering/skills/minecraft-staff-operations/SKILL.md) | Staff roles, onboarding, permissions, training, escalation, accountability, and offboarding |
| [`minecraft-player-support`](plugins/minecraft-server-engineering/skills/minecraft-player-support/SKILL.md) | Tickets, access problems, bugs, restorations, purchases, support evidence, and escalation |
| [`minecraft-events-liveops`](plugins/minecraft-server-engineering/skills/minecraft-events-liveops/SKILL.md) | Seasons, tournaments, launches, limited-time events, staffing, load preparation, and closeout |
| [`minecraft-capacity-cost-planning`](plugins/minecraft-server-engineering/skills/minecraft-capacity-cost-planning/SKILL.md) | Hardware/hosting sizing, headroom, scaling, storage/network growth, DR cost, and budget decisions |
| [`minecraft-documentation-change-management`](plugins/minecraft-server-engineering/skills/minecraft-documentation-change-management/SKILL.md) | Runbooks, SOPs, architecture records, maintenance plans, production changes, and handoffs |
| [`minecraft-store-commerce`](plugins/minecraft-server-engineering/skills/minecraft-store-commerce/SKILL.md) | Store purchases, paid entitlements, fulfillment, refunds, chargebacks, fraud controls, and policy checks |
| [`minecraft-analytics-product-ops`](plugins/minecraft-server-engineering/skills/minecraft-analytics-product-ops/SKILL.md) | KPIs, retention cohorts, telemetry, progression/economy analytics, feature evaluation, and experiments |

## Router

[`index`](plugins/minecraft-server-engineering/skills/index/SKILL.md) is the plugin-level entry point. It routes broad or multi-domain requests to the smallest relevant set of specialist skills and defines cross-cutting safety rules.

## Operating principles

1. Identify exact versions, topology, persistent state, player impact, and current health before changing production.
2. Treat compatibility and platform policy as version-specific; verify current authoritative sources when they matter.
3. Back up before destructive, migration, economy, world, schema, or upgrade work.
4. Use least privilege for OS, panel, RCON, database, CI, bots, plugin permissions, and staff roles.
5. Keep secrets and sensitive player data out of commits and unnecessary output.
6. Never block latency-sensitive game threads with avoidable I/O or expensive work.
7. Measure before optimizing and separate evidence from inference.
8. Define rollback, verification, ownership, and escalation for risky production changes.

## Future app/MCP layer

A later release can add optional app/MCP integrations for RCON, Pterodactyl or other panels, GitHub, Discord, Prometheus/Grafana, databases, object storage, and deployment systems. Those integrations should preserve source-system authorization and use explicit confirmation/least-privilege controls for write actions.
