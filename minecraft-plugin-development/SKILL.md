---
name: minecraft-plugin-development
description: Design and implement production-grade Minecraft server plugins with safe lifecycle handling, commands, events, schedulers, configuration, APIs, and version-aware platform integration.
---

# Minecraft Plugin Development

Use this skill when creating or modifying Bukkit/Spigot/Paper/Purpur-family plugins or comparable server-side extensions.

## Establish the target

Before coding, identify the exact server implementation, Minecraft version range, Java version, build system, API dependency, required integrations, concurrency model, and deployment environment. Do not assume an API exists on every implementation or version.

## Development rules

- Keep plugin enable/disable lifecycle deterministic and idempotent.
- Fail startup clearly when required configuration or dependencies are invalid.
- Register commands, listeners, services, and tasks explicitly; cancel or close owned resources on disable.
- Keep blocking I/O, HTTP, database work, filesystem scans, and expensive computation off latency-sensitive server threads.
- Marshal game-state mutation back to the scheduler/context required by the target platform.
- Avoid static global state unless its lifetime and reset behavior are intentional.
- Validate player-controlled input and never trust display names as identities; use stable identifiers where appropriate.
- Store configuration with defaults, validation, migrations, and actionable error messages.
- Prefer stable public APIs over internal server classes; isolate unavoidable implementation-specific code behind adapters.

## Feature workflow

1. write the behavioral contract and failure cases;
2. define commands/permissions/events/data changes;
3. implement the smallest vertical slice;
4. add automated tests for pure logic;
5. test on an isolated server with the exact target stack;
6. inspect startup/shutdown logs and reload/restart behavior;
7. profile hot paths under representative load;
8. document configuration, permissions, data migrations, and rollback.

## Completion criteria

A plugin change is incomplete until build reproducibility, dependency resolution, permission behavior, persistence, restart behavior, error handling, performance impact, and upgrade/rollback behavior have been verified.