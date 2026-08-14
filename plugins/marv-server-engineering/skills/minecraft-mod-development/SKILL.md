---
name: minecraft-mod-development
description: Develop and maintain Minecraft server or shared mods with loader-aware architecture, mappings/API compatibility, side separation, networking, persistence, testing, and upgrade-safe packaging.
---

# Minecraft Mod Development

Use this skill for Fabric/Forge/NeoForge-style mods or other loader-based Minecraft extensions.

## Establish the matrix

Identify exact Minecraft version, loader and loader version, mappings/toolchain, Java version, server-only versus client-required behavior, dependency mods, mixins/access wideners/transformations, and distribution constraints.

## Engineering rules

- Keep client-only classes and rendering APIs out of dedicated-server execution paths.
- Validate network packets, direction, size, and authorization before mutating state.
- Treat mixins/transformations as high-coupling code: keep targets narrow and test on every supported version.
- Version saved data and configuration with explicit migrations.
- Avoid blocking I/O on game threads.
- Respect loader lifecycle and registry timing rather than relying on accidental initialization order.
- Isolate loader-specific code from domain logic when maintaining multiple loaders.
- Test dedicated-server startup without client classes present.

## Release checks

Verify clean server boot, world creation/load, save/restart persistence, client compatibility where required, networking, dependency failure behavior, upgrade from prior versions, and removal/rollback expectations.