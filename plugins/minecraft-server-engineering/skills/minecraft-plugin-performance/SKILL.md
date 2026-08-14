---
name: minecraft-plugin-performance
description: Engineer and profile Minecraft plugin performance by controlling tick-thread work, allocation, I/O, event frequency, scheduler load, database access, caching, and algorithmic complexity.
---

# Minecraft Plugin Performance

Use this skill when a plugin may affect TPS/MSPT, memory, GC, scheduler load, network usage, or database latency.

## Rules

- Measure before optimizing; identify the plugin method, event, task, or query consuming time.
- Treat high-frequency events as hot paths and minimize allocations, scans, lookups, and logging inside them.
- Never perform blocking database, HTTP, DNS, or slow filesystem operations on latency-sensitive server threads.
- Batch work where semantics permit and bound every queue/cache.
- Avoid scanning all players/entities/chunks when an indexed or event-driven design can maintain the required state.
- Cache only when invalidation and memory limits are explicit.
- Use prepared statements and indexes for repeated database access; inspect query plans when data volume grows.
- Avoid creating one repeating task per entity/player when one bounded coordinator can do the same work.

## Performance review

Capture baseline MSPT/TPS, CPU, allocation/GC, heap, task timings, query latency, and representative player/entity counts. Profile under realistic load, change one cause at a time, then repeat the same measurements.

Performance fixes must preserve gameplay correctness; skipping persistence, authorization, or consistency checks to gain speed is not an acceptable optimization.