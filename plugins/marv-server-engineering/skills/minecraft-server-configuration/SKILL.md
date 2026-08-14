---
name: minecraft-server-configuration
description: Design, review, and safely change Minecraft server, proxy, plugin, mod, JVM, and service configuration with validation, version control, staged rollout, and rollback.
---

# Minecraft Server Configuration

Use this skill for configuration design and changes that are not primarily code changes.

## Configuration inventory

Map server properties, implementation-specific settings, proxy configuration, plugin/mod configs, permissions, JVM/service/container settings, environment variables, secrets, and generated files. Identify which component owns each value and whether restart/reload is required.

## Change rules

- Never edit production configuration without preserving the prior version or a reproducible source of truth.
- Validate syntax and value ranges before activation.
- Treat configuration schemas as version-specific; check upstream documentation for the exact target version.
- Separate secrets from normal version-controlled configuration.
- Avoid broad copy/paste tuning bundles whose assumptions are unknown.
- Change one causal group at a time when diagnosing behavior.
- Prefer immutable/reproducible configuration over undocumented panel-only drift.

## Workflow

1. capture current effective configuration and baseline health;
2. define intended behavior and affected components;
3. review the diff, compatibility, and restart impact;
4. create a backup/rollback point;
5. stage the change;
6. activate using the component's supported reload/restart path;
7. verify logs, joinability, gameplay paths, persistence, and performance;
8. record the effective change and remove temporary overrides.

Do not use plugin/server reload mechanisms known to leave lifecycle state ambiguous unless the specific component explicitly supports them.