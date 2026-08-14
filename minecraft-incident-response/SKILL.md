---
name: minecraft-incident-response
description: Respond to Minecraft server incidents such as crash loops, failed deploys, world/data corruption, resource exhaustion, dependency failures, and proxy/network outages using containment, evidence preservation, recovery, and post-incident analysis.
---

# Minecraft Incident Response

Use this skill when availability, integrity, or player-facing service is actively degraded.

## Priorities

1. protect player/world data;
2. stop the incident from getting worse;
3. preserve enough evidence to identify cause;
4. restore the simplest known-good service state;
5. verify data integrity and gameplay paths;
6. document timeline, cause, and follow-up actions.

Prefer recovery over experimentation on the only production copy.

## Initial triage

Record immediately:

```text
incident start / detection time
user-visible symptom
servers/proxies affected
last known-good time
recent deploy/config/plugin/mod changes
process/restart status
first relevant error and first Caused by
TPS/MSPT before failure if available
CPU/RAM/swap/disk/inodes
backup freshness
external dependency status
```

Take a copy of critical logs/config and crash reports before repeated retries overwrite or rotate evidence.

## Containment

Examples of safe containment:

- stop an automated crash/restart loop while diagnosing;
- remove the failed node from proxy traffic if the network has redundant capacity;
- enable maintenance/whitelist mode when continued writes threaten integrity;
- freeze deploys and configuration automation;
- stop nonessential heavy jobs such as pregeneration or backups if they are exhausting resources;
- isolate a suspected newly deployed artifact by rolling back to the known-good version.

Do not delete corrupted files, crash reports, or failed artifacts before preserving a copy.

## Crash loop

1. stop the restart loop;
2. inspect the first crash from process start, not only the latest repeated crash;
3. classify: Java/runtime, plugin/mod dependency, config syntax, port binding, filesystem/permission, OOM, disk, world load, database, or host issue;
4. compare against the last known-good deployment/config;
5. apply the smallest reversible fix or rollback;
6. start once under observation;
7. verify stability before reenabling automatic restarts/traffic.

## Failed deployment

If failure follows a deploy and no irreversible migration is required, rollback first when that is lower risk than live debugging. Restore data only when the failed deployment changed persistent formats/state and a consistent pre-change backup is required.

## Disk or inode exhaustion

Do not immediately delete world/player/plugin data. Identify growth sources such as logs, backups, crash dumps, maps, pregenerated chunks, or container layers. Free space from clearly disposable/rotatable data according to retention policy, then verify filesystem writability and server persistence.

## Suspected world/data corruption

- stop new writes or isolate the affected world/node;
- preserve the current broken state;
- identify the smallest corrupted scope from logs and reproduction;
- prefer restore from a verified recovery point over ad-hoc binary editing;
- test restoration on a copy when possible;
- verify playerdata, dimensions, chunks, inventories, permissions, and plugin databases before reopening.

## Network/proxy incident

Separate layers:

- client -> edge/proxy;
- proxy -> backend;
- backend -> database/cache/external service;
- DNS/firewall/load balancer/provider.

Check reachability, listener state, proxy logs, backend registration, forwarding/authentication configuration, RTT/loss, and recent network changes. A healthy backend TPS does not prove the player path is healthy.

## Recovery verification

Before declaring recovery:

- process remains stable beyond one restart cycle;
- no recurring critical error;
- representative client can join through the normal proxy/edge path;
- world changes persist across a controlled save/restart when appropriate;
- critical plugin/mod state is intact;
- TPS/MSPT and host metrics returned to baseline range;
- backups resumed and the next backup succeeds;
- temporary containment controls are intentionally kept or removed.

## Post-incident record

Write a concise timeline with:

```text
impact
start/detect/mitigate/recover times
root cause or best-supported causal chain
contributing factors
why safeguards did/did not catch it
actions taken
rollback/recovery point used
verification evidence
follow-ups with owner/priority
```

Distinguish root cause from trigger and from contributing conditions. Avoid attributing cause without evidence.
