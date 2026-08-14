---
name: minecraft-observability
description: Observe and diagnose Minecraft server health using TPS/MSPT, JVM and host metrics, disk/network signals, logs, alerts, and low-overhead profiling.
---

# Minecraft Observability

Use this skill to answer: "Is the server healthy?", "What changed?", and "Where is latency or instability coming from?"

## Core model

Minecraft's main simulation loop targets 20 ticks per second, giving a 50 ms budget per tick. Sustained MSPT above 50 ms means the server cannot maintain 20 TPS. Treat TPS as an outcome metric and MSPT/profile data as stronger diagnostic evidence.

Correlate four layers instead of diagnosing from one graph:

1. **Minecraft:** TPS, MSPT, tick percentiles, player count, chunks/entities, scheduled tasks, plugin/mod timings.
2. **JVM:** heap used/committed/max, allocation rate, GC frequency and pause time, thread state, safepoints when available.
3. **Host/container:** CPU per core, steal/throttling, memory pressure, swap, disk latency/space/inodes, file descriptors.
4. **Network/dependencies:** RTT, packet loss, proxy/backend connectivity, DNS, database/cache latency, external APIs.

## Minimum triage snapshot

Record the timestamp and gather:

```text
server role/version + Java version
player count and recent change
TPS/MSPT (including percentiles if available)
CPU and CPU throttling/steal
heap and GC behavior
RAM/swap pressure
disk free + inode free + disk latency if available
network errors/latency
recent WARN/ERROR/FATAL/repeating exceptions
deploy/config/plugin changes near incident start
```

## Log triage

Prioritize patterns by causal value:

- crash exception and first `Caused by`, not only the final wrapper stack trace;
- watchdog/tick timeout messages;
- out-of-memory or native allocation failures;
- disk full, read-only filesystem, permission, or I/O exceptions;
- plugin/mod load failures and dependency/version mismatches;
- database timeouts/locks and connection-pool exhaustion;
- proxy forwarding/authentication errors;
- repeated chunk/entity serialization errors;
- long GC pauses or JVM fatal error files.

Avoid flooding output with entire logs. Extract the first occurrence, surrounding context, recurrence count, and timestamps.

## Profiling

Prefer a profiler designed for the running server implementation (for example, spark when installed and compatible) and use the lowest overhead mode that can answer the question.

Profile during the problem window. Capture:

- wall-clock/tick hotspots;
- plugin/mod ownership of hot methods;
- entity/chunk counts where relevant;
- GC/memory allocation evidence if the symptom suggests memory pressure.

Do not interpret a profile taken during empty-server idle as proof about peak-load lag.

## Alert heuristics

Use sustained windows and baselines; avoid paging on one-tick spikes. Useful conditions include:

- sustained MSPT approaching/exceeding 50 ms;
- repeated watchdog stalls;
- crash/restart loops;
- low disk or inode headroom;
- unexpected swap or memory-limit pressure;
- GC pauses correlated with tick stalls;
- rapid log error-rate increase;
- proxy/backend disconnect rate increase;
- backup failures or stale successful-backup age.

Thresholds other than Minecraft's 50 ms tick budget should be tuned from the environment's normal baseline and SLOs.

## Reporting

Separate facts from hypotheses:

```text
Observed:
- ...

Correlated changes:
- ...

Most likely bottleneck:
- ...

Evidence:
- ...

Next discriminating test:
- ...
```

Avoid claiming a plugin, JVM flag, host, or network is the root cause without evidence that distinguishes it from alternatives.
