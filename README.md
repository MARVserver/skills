# MARVserver Skills

A production-oriented Minecraft server engineering and operations skill set for AI agents.

The repository covers the full server lifecycle: plugin/mod/content development, architecture and testing, configuration and network design, permissions/security, gameplay/economy, reliability engineering, moderation, community/staff/support operations, live events, commerce, analytics, and capacity/cost management.

The guidance is version-aware and implementation-aware, but intentionally avoids assuming one hosting provider or one exact Minecraft/server version. Check authoritative upstream documentation for compatibility-sensitive changes.

## Development and engineering

| Skill | Use it for |
| --- | --- |
| [`minecraft-plugin-development`](minecraft-plugin-development/SKILL.md) | Commands, events, schedulers, lifecycle, configuration, APIs, and production plugin implementation |
| [`minecraft-plugin-architecture`](minecraft-plugin-architecture/SKILL.md) | Domain/service/platform boundaries, lifecycle ownership, adapters, and maintainable plugin design |
| [`minecraft-plugin-testing-debugging`](minecraft-plugin-testing-debugging/SKILL.md) | Unit/integration tests, isolated server tests, bug reproduction, stack traces, and regression coverage |
| [`minecraft-plugin-performance`](minecraft-plugin-performance/SKILL.md) | Tick-thread load, hot events, allocation, queues, I/O, queries, caching, and plugin profiling |
| [`minecraft-plugin-data-integrations`](minecraft-plugin-data-integrations/SKILL.md) | SQL, embedded databases, caches, HTTP APIs, bots, message systems, and cross-server state |
| [`minecraft-plugin-security`](minecraft-plugin-security/SKILL.md) | Authorization, untrusted input, secrets, SQL/file safety, rate limits, and abuse-resistant plugin code |
| [`minecraft-plugin-release-compatibility`](minecraft-plugin-release-compatibility/SKILL.md) | CI/builds, artifacts, compatibility matrices, migrations, releases, changelogs, and rollback |
| [`minecraft-mod-development`](minecraft-mod-development/SKILL.md) | Loader-aware mod development, side separation, networking, mappings, persistence, and packaging |
| [`minecraft-datapack-resourcepack-automation`](minecraft-datapack-resourcepack-automation/SKILL.md) | Datapacks, resource packs, functions, generated content, validation, performance, and deployment |

## Server platform and gameplay

| Skill | Use it for |
| --- | --- |
| [`minecraft-server-configuration`](minecraft-server-configuration/SKILL.md) | Server/proxy/plugin/mod/JVM/service configuration, diffs, validation, activation, and rollback |
| [`minecraft-network-proxy`](minecraft-network-proxy/SKILL.md) | Proxies, routing, backend isolation, forwarding/authentication, DNS, firewalls, and failover |
| [`minecraft-permissions-access-control`](minecraft-permissions-access-control/SKILL.md) | Permission groups, staff/admin capabilities, console/panel access, service accounts, and audits |
| [`minecraft-world-content-management`](minecraft-world-content-management/SKILL.md) | Worlds, dimensions, resets, pregeneration, maps, migration, regions, and content rollout |
| [`minecraft-gameplay-economy`](minecraft-gameplay-economy/SKILL.md) | Virtual currencies, rewards, shops, progression, sources/sinks, exploit controls, and balance |
| [`minecraft-anti-cheat-abuse-prevention`](minecraft-anti-cheat-abuse-prevention/SKILL.md) | Anti-cheat signals, exploits, duplication, botting, false positives, containment, and evidence |
| [`minecraft-security-privacy`](minecraft-security-privacy/SKILL.md) | Host/service hardening, secrets, patching, audit logs, player-data minimization, and access review |

## Reliability and DevOps

| Skill | Use it for |
| --- | --- |
| [`minecraft-server-operations`](minecraft-server-operations/SKILL.md) | Start/stop/restart, console operations, health checks, routine maintenance, and safe admin work |
| [`minecraft-deployments`](minecraft-deployments/SKILL.md) | Server/proxy/plugin/mod/config/Java rollouts with compatibility checks, staged verification, and rollback |
| [`minecraft-observability`](minecraft-observability/SKILL.md) | TPS/MSPT, JVM, host, disk, network, logs, alert triage, and profiling |
| [`minecraft-backup-recovery`](minecraft-backup-recovery/SKILL.md) | Consistent backups, retention, off-host copies, restore drills, and disaster recovery |
| [`minecraft-performance`](minecraft-performance/SKILL.md) | Server-wide lag diagnosis and evidence-based tuning of chunks, entities, JVM, host, plugins, and mods |
| [`minecraft-incident-response`](minecraft-incident-response/SKILL.md) | Crash loops, corruption, failed deploys, exhaustion, dependency/network incidents, containment, and recovery |

## LiveOps and server management

| Skill | Use it for |
| --- | --- |
| [`minecraft-moderation`](minecraft-moderation/SKILL.md) | Warnings, mutes, bans, evidence review, appeals, proportional enforcement, and moderator quality |
| [`minecraft-community-management`](minecraft-community-management/SKILL.md) | Announcements, feedback loops, onboarding, community channels, roadmap communication, and community health |
| [`minecraft-staff-operations`](minecraft-staff-operations/SKILL.md) | Staff roles, onboarding, permissions, training, escalation, accountability, and offboarding |
| [`minecraft-player-support`](minecraft-player-support/SKILL.md) | Tickets, access problems, bugs, restorations, purchases, support evidence, and escalation |
| [`minecraft-events-liveops`](minecraft-events-liveops/SKILL.md) | Seasons, tournaments, launches, limited-time events, staffing, load preparation, and closeout |
| [`minecraft-capacity-cost-planning`](minecraft-capacity-cost-planning/SKILL.md) | Hardware/hosting sizing, headroom, scaling, storage/network growth, DR cost, and budget decisions |
| [`minecraft-documentation-change-management`](minecraft-documentation-change-management/SKILL.md) | Runbooks, SOPs, architecture records, maintenance plans, production changes, and handoffs |
| [`minecraft-store-commerce`](minecraft-store-commerce/SKILL.md) | Store purchases, paid entitlements, fulfillment, refunds, chargebacks, fraud controls, and policy checks |
| [`minecraft-analytics-product-ops`](minecraft-analytics-product-ops/SKILL.md) | KPIs, retention cohorts, telemetry, progression/economy analytics, feature evaluation, and experiments |

## Operating principles

1. **Identify before changing.** Establish exact server role, implementation/version, Java/runtime, dependencies, launch method, persistent data, player impact, and current health.
2. **Treat compatibility as version-specific.** Verify authoritative upstream documentation and release notes instead of assuming APIs/configuration/policies are unchanged.
3. **Protect persistent state.** Back up before destructive, migration, upgrade, economy, world, or schema changes; test restoration for important systems.
4. **Use least privilege.** Minimize OS, panel, RCON, database, bot, CI, plugin permission, and staff access.
5. **Keep secrets and sensitive player data out of commits/output.** Redact credentials and minimize copied moderation/support/analytics data.
6. **Do not block latency-sensitive game threads.** Move blocking I/O and expensive work to appropriate execution contexts, then return game-state mutation through the platform-safe scheduler/context.
7. **Measure before optimizing.** Use reproducible baselines, profiling, metrics, and controlled comparisons.
8. **Make risky changes reversible.** Define success criteria, rollback triggers, rollback procedure, and post-change verification before production activation.
9. **Separate evidence from inference.** This applies to debugging, incidents, anti-cheat, moderation, analytics, and capacity decisions.
10. **Document operational ownership.** Important systems need an owner, runbook, escalation path, and recovery procedure.

## Repository layout

Each skill is self-contained in:

```text
<skill-name>/SKILL.md
```

Every `SKILL.md` uses YAML front matter with `name` and `description`, followed by task-specific operating instructions.

## Coverage

The current catalog contains **31 skills** spanning engineering through day-to-day server management. Individual plugin/provider/payment/legal/platform requirements can change; when a task depends on those details, verify the current authoritative source before acting.
