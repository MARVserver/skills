---
name: minecraft-world-content-management
description: Manage Minecraft worlds, dimensions, seeds, pregeneration, borders, resets, migrations, maps, regions, schematics, and content rollouts while protecting persistent player data.
---

# Minecraft World and Content Management

Use this skill for world lifecycle, map releases, resets, pregeneration, region repair, transfers, and large content changes.

## World inventory

Identify every active dimension/world, generator, seed/config, border, spawn, plugin-owned world metadata, playerdata relationship, claims/regions, map renderer, and backup coverage.

## Safe operations

- Back up before reset, trim, migration, repair, pregeneration reconfiguration, or bulk schematic operations.
- Confirm which folders belong to which worlds; do not delete by guessed names.
- Quiesce writes before filesystem-level moves or restores.
- Test custom generators and datapacks on a copy before opening production generation.
- Bound pregeneration concurrency and disk growth; observe CPU, memory, disk I/O, and free space.
- Treat game-version downgrades or world-format rollback as unsupported unless explicitly validated upstream.

## Release/reset plan

Define player-facing scope, preserved versus reset data, spawn/portal behavior, claims/economy dependencies, downtime, backup point, migration scripts, and rollback. Verify joins, dimensions, inventories, claims, teleport destinations, map data, saving, and restart persistence before reopening.

For corruption, preserve the damaged copy before region-level repair or selective restoration.