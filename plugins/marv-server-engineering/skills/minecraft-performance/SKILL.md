---
name: minecraft-performance
description: Diagnose and improve Minecraft server performance using controlled measurements, profiling, and safe tuning across chunks, entities, plugins/mods, JVM behavior, storage, and CPU constraints.
---

# Minecraft Performance Engineering

Use this skill for lag, low TPS, high MSPT, stutter, GC pauses, slow chunk loads, or capacity planning.

## Rule: measure before tuning

Do not start by copying generic JVM flags or changing ten server settings. Establish a reproducible baseline under representative load.

Capture:

- implementation/Minecraft/Java versions;
- player count and workload pattern;
- TPS and MSPT distribution;
- CPU utilization per relevant core and throttling/steal;
- heap occupancy, allocation rate, GC frequency/pause time;
- disk I/O latency and available space;
- chunk/entity/tile/block-entity counts when available;
- plugin/mod profiler hotspots;
- view distance, simulation distance, world generation/pregeneration state;
- recent deployments/config changes.

## Bottleneck decision tree

### MSPT high, one core saturated

Suspect main-thread work: entities, chunks, redstone, plugin/mod tasks, synchronous I/O, world generation, or expensive commands. Use a tick-aware profiler to find ownership before tuning.

### MSPT spikes correlate with GC

Inspect heap sizing, allocation rate, plugin/mod allocation hotspots, container memory limit, and whether the host is swapping. More heap is not automatically better; oversized heaps can change pause/recovery behavior and hide leaks.

### Chunk exploration causes lag

Measure world generation and chunk I/O. Consider pregeneration for bounded exploration areas, reasonable view/simulation distances, and storage performance. Validate disk headroom before large pregeneration jobs.

### TPS looks normal but players report lag

Check network RTT/loss, proxy routing, packet-heavy plugins/mods, client-side performance, and dependency latency. Do not equate 20 TPS with end-to-end player experience.

### Performance degrades over hours/days

Look for memory leaks, entity accumulation, chunk tickets, scheduled task growth, database queues, log growth/disk pressure, and resource leaks.

## Controlled optimization loop

For each candidate change:

1. state the hypothesis;
2. choose one primary metric and guardrail metrics;
3. capture a baseline window;
4. change one causal variable;
5. repeat the same workload/window;
6. compare median and tail behavior, not only one sample;
7. keep the change only if improvement is material and no guardrail regresses;
8. document result and rollback.

## Common levers

Evaluate, rather than blindly apply:

- simulation distance and view distance;
- entity activation/tracking ranges and mob caps where implementation supports them;
- redstone/hopper/villager/farm workload;
- chunk pregeneration and world border strategy;
- plugin/mod replacement, configuration, task scheduling, and database access;
- async-safe workloads supported by the implementation;
- storage latency and filesystem/container constraints;
- CPU single-thread performance and host oversubscription;
- Java version and implementation-supported JVM configuration;
- memory limit/heap relationship.

Always check current upstream documentation because keys and recommended defaults change across server versions.

## Unsafe shortcuts

Avoid:

- deleting entities/chunks as a first diagnostic step;
- disabling watchdogs to hide stalls;
- allocating nearly all host RAM to Java and starving the OS/page cache;
- unreviewed "optimization" scripts that rewrite many config values;
- production load tests that can exhaust disk, CPU, memory, or network;
- blaming a plugin based only on its presence rather than profile evidence.

## Performance report

Provide before/after values, workload, profiler evidence, exact configuration diff, tradeoffs, and whether the change affects gameplay semantics.
