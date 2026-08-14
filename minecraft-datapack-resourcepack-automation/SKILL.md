---
name: minecraft-datapack-resourcepack-automation
description: Build, validate, deploy, and operate Minecraft datapacks, resource packs, command/function automation, generated content, and pack delivery with versioned assets and safe rollback.
---

# Minecraft Datapack, Resource Pack, and Automation

Use this skill for functions, tags, recipes, loot tables, predicates, advancements, worldgen data, resource assets, generated pack content, and server automation built around them.

## Workflow

1. identify the exact pack/game format and target versions;
2. keep source assets separate from generated output;
3. validate JSON/data structure and references before deployment;
4. lint functions and generated identifiers where tooling permits;
5. test in an isolated world/profile;
6. measure expensive functions or selectors under representative entity/player counts;
7. package deterministically and record a checksum;
8. deploy with backup and rollback.

## Safety

Avoid unbounded per-tick command chains, broad selectors, recursive functions without limits, destructive world operations without backups, and generated assets that overwrite hand-authored source. For resource-pack delivery, version URLs/artifacts so clients do not receive ambiguous cached content.

Document required server settings, load order/dependencies, operator commands, and removal behavior.