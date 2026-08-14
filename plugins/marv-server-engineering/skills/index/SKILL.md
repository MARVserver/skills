---
name: index
description: Route broad or multi-domain Minecraft server engineering and operations requests to the appropriate bundled skills. Use when this plugin is explicitly invoked or when a request spans development, infrastructure, reliability, security, LiveOps, moderation, commerce, or analytics.
---

# Minecraft Server Engineering Router

Use this skill as the plugin-level entry point. Select the smallest set of specialist skills that fully covers the task.

## Routing rules

1. If the user names a specific bundled skill or clearly asks for one narrow domain, use that specialist skill directly.
2. For broad requests, classify the work before acting: development, platform/gameplay, reliability/DevOps, or LiveOps/management.
3. For cross-domain work, order the skills by dependency: architecture/context -> implementation/configuration -> testing/security -> deployment/operations -> observability/verification.
4. When exact Minecraft, Java, server implementation, loader, proxy, plugin, payment, or platform-policy behavior may have changed, verify the current authoritative source before relying on version-sensitive details.
5. Before destructive or production-changing work, establish backup/rollback and concrete verification criteria.
6. Do not claim an external action was performed unless the runtime actually provides the required tool and authorization.

## Development and engineering routes

- `minecraft-plugin-development`: Paper/Purpur-style plugin implementation, commands, events, schedulers, lifecycle, config, APIs.
- `minecraft-plugin-architecture`: maintainable boundaries, services, adapters, lifecycle ownership, dependency design.
- `minecraft-plugin-testing-debugging`: tests, reproduction, stack traces, regression coverage, isolated server testing.
- `minecraft-plugin-performance`: plugin-specific profiling, tick-thread cost, I/O, allocation, queries, caching.
- `minecraft-plugin-data-integrations`: SQL, caches, HTTP APIs, bots, messaging, cross-server state.
- `minecraft-plugin-security`: authorization, input handling, secrets, SQL/filesystem safety, abuse resistance.
- `minecraft-plugin-release-compatibility`: CI, artifacts, compatibility, migrations, releases, changelogs, rollback.
- `minecraft-mod-development`: loader-aware mod work, side separation, networking, mappings, persistence, packaging.
- `minecraft-datapack-resourcepack-automation`: datapacks, resource packs, functions, generated assets/content, deployment.

For a new production plugin, normally combine architecture + development + testing/debugging; add security, performance, data integrations, and release/compatibility when relevant.

## Server platform and gameplay routes

- `minecraft-server-configuration`: server/proxy/plugin/mod/JVM/service configuration and safe activation.
- `minecraft-network-proxy`: proxy topology, routing, forwarding/authentication, backend isolation, DNS/firewalls/failover.
- `minecraft-permissions-access-control`: permission groups, admin/staff capabilities, console/panel/service-account access.
- `minecraft-world-content-management`: worlds/dimensions, resets, pregeneration, maps, regions, migrations.
- `minecraft-gameplay-economy`: currencies, rewards, shops, progression, sources/sinks, exploit controls and balance.
- `minecraft-anti-cheat-abuse-prevention`: detections, exploits, duplication, botting, evidence, false positives, containment.
- `minecraft-security-privacy`: infrastructure hardening, secrets, patching, audit logs and player-data minimization.

## Reliability and DevOps routes

- `minecraft-server-operations`: routine administration, graceful control, console work, maintenance and health checks.
- `minecraft-deployments`: server/proxy/plugin/mod/config/Java rollout, staging, smoke tests and rollback.
- `minecraft-observability`: TPS/MSPT, JVM, host, disk, network, logs, alerts and profiling.
- `minecraft-backup-recovery`: consistency, retention, off-host copies, restore drills and disaster recovery.
- `minecraft-performance`: server-wide lag diagnosis and evidence-based tuning.
- `minecraft-incident-response`: crash loops, corruption, failed deploys, resource/network/dependency incidents and recovery.

For an active outage, start with incident response; use observability to gather evidence and backup/recovery only when restoration is part of the recovery path.

## LiveOps and management routes

- `minecraft-moderation`: warnings, mutes, bans, evidence review, appeals and proportional enforcement.
- `minecraft-community-management`: announcements, feedback loops, onboarding, roadmap communication and community health.
- `minecraft-staff-operations`: roles, onboarding, training, escalation, accountability and offboarding.
- `minecraft-player-support`: tickets, access issues, bugs, restorations, purchases and escalation.
- `minecraft-events-liveops`: seasons, tournaments, launches, limited-time events, staffing and load preparation.
- `minecraft-capacity-cost-planning`: hardware/hosting sizing, headroom, scaling, storage/network growth, DR and budget.
- `minecraft-documentation-change-management`: runbooks, SOPs, architecture records, maintenance plans and handoffs.
- `minecraft-store-commerce`: paid entitlements, fulfillment, refunds, chargebacks, fraud controls and policy checks.
- `minecraft-analytics-product-ops`: KPIs, cohorts, telemetry, feature evaluation, economy/progression analytics and experiments.

## Cross-cutting production rules

- Identify exact versions, topology, dependencies, launch method, persistent state, current health and player impact.
- Protect worlds, player state, plugin/mod data, configuration and authoritative external databases before risky changes.
- Use least privilege and keep credentials/private player data out of commits and unnecessary output.
- Never move blocking I/O or expensive work onto latency-sensitive game threads when a safe asynchronous pattern exists.
- Prefer reversible changes, small blast radius, staged rollout and explicit rollback triggers.
- Separate observed evidence from inference in debugging, incidents, anti-cheat, moderation and analytics.
- A production change is incomplete until health, joinability, persistence, logs and relevant gameplay/business paths are verified.
