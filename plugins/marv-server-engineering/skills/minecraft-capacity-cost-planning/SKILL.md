---
name: minecraft-capacity-cost-planning
description: Plan Minecraft server capacity and infrastructure cost using workload measurements, concurrency forecasts, headroom, scaling boundaries, storage growth, backup costs, and failure-domain tradeoffs.
---

# Minecraft Capacity and Cost Planning

Use this skill for hardware sizing, hosting changes, network growth, budget tradeoffs, and expected player-concurrency increases.

## Measure the workload

Capture peak/typical concurrent players, MSPT/TPS, single-core and total CPU utilization, heap/GC, memory pressure, disk latency/throughput, network throughput, world/storage growth, plugin/database latency, and backup duration.

## Planning rules

- Size from observed bottlenecks; Minecraft workloads are not reducible to RAM alone.
- Preserve operational headroom for bursts, chunk generation, saves, backups, GC, and failover.
- Distinguish vertical scaling limits from workloads that can be split across backends/proxies.
- Include storage snapshots, off-host backups, database, traffic, observability, and disaster-recovery costs.
- Model expected growth and a high-but-plausible event peak, not only current averages.
- Avoid increasing resources as a substitute for fixing pathological plugin or world behavior.

## Decision record

For each capacity change record baseline, bottleneck, alternatives, expected improvement, monthly/annual cost, migration risk, rollback, and the metric that will prove whether the purchase solved the problem.