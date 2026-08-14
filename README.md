# MARVserver Skills

Operational skills for AI agents working on Minecraft server infrastructure.

The initial set focuses on production-safe Java Edition server DevOps: routine operations, deployments, observability, backups and restore, performance work, and incident response. The guidance is implementation-aware (Paper/Purpur/Fabric/Forge/NeoForge, Velocity/Bungee-style proxies, systemd, containers) but avoids assuming a particular hosting stack.

## Skills

| Skill | Use it for |
| --- | --- |
| [`minecraft-server-operations`](minecraft-server-operations/SKILL.md) | Start/stop/restart, console operations, health checks, configuration changes, and routine maintenance |
| [`minecraft-deployments`](minecraft-deployments/SKILL.md) | Server jar, proxy, plugin/mod, configuration, and Java runtime rollouts with rollback planning |
| [`minecraft-observability`](minecraft-observability/SKILL.md) | TPS/MSPT, JVM, host, disk, network, logs, alert triage, and profiling |
| [`minecraft-backup-recovery`](minecraft-backup-recovery/SKILL.md) | Consistent backups, retention, restore drills, and disaster recovery |
| [`minecraft-performance`](minecraft-performance/SKILL.md) | Lag diagnosis and evidence-based tuning of chunks, entities, plugins/mods, JVM, and host resources |
| [`minecraft-incident-response`](minecraft-incident-response/SKILL.md) | Crash loops, corruption, failed deploys, resource exhaustion, network incidents, containment, and recovery |

## Operating principles

1. **Identify before changing.** Establish server implementation/version, Java runtime, launch method, filesystem layout, player impact, and current health first.
2. **Prefer graceful control paths.** Use the server console/RCON or the service manager before signals; avoid `kill -9` except for an unrecoverably wedged process.
3. **Back up before destructive or hard-to-reverse work.** Include worlds, configs, plugin/mod data, permissions, and external databases where applicable.
4. **Make one causal change at a time.** Capture a baseline, change the smallest relevant variable, then verify with the same measurements.
5. **Treat compatibility as version-specific.** Check authoritative upstream release notes/documentation for Minecraft, Java, server implementation, proxy, plugins, and mods before upgrades.
6. **Keep secrets out of output and commits.** Redact RCON passwords, panel/API tokens, database credentials, private addresses, and player-sensitive data.
7. **Always define rollback and verification.** A change is incomplete until health, joinability, world persistence, logs, and key gameplay paths are checked.

## Layout

Each skill is self-contained in `<skill-name>/SKILL.md` and uses YAML front matter with `name` and `description` followed by operational instructions.

## Scope

These skills cover operations and reliability engineering. They are not a substitute for host/provider policies, plugin-specific documentation, security review, or tested backups.
