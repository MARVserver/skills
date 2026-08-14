---
name: minecraft-deployments
description: Plan and execute safe Minecraft server, proxy, plugin/mod, configuration, and Java runtime deployments with compatibility checks, backups, staged rollout, verification, and rollback.
---

# Minecraft Deployments

Use this skill for production changes that alter executable artifacts, plugins/mods, proxies, configuration, Java, or the launch/runtime environment.

## Deployment contract

Every deployment should have:

- explicit target nodes and server roles;
- exact current and target versions;
- authoritative compatibility evidence for Minecraft, Java, server implementation, proxy, plugins/mods, and protocol bridges;
- a pre-change backup or snapshot appropriate to the risk;
- artifact provenance and checksum where practical;
- a rollback plan with known-good artifacts/config;
- maintenance/canary strategy;
- concrete success criteria.

Do not infer that a plugin/mod is compatible merely because it loads. Check upstream release notes and compatibility statements for the exact target versions.

## Preflight

Capture:

```text
server implementation + version
Minecraft version
Java vendor + major version
plugins/mods + versions
proxy/protocol translation components
launch flags and memory limits
world/data format considerations
free disk space
backup status
```

Check for breaking changes in configuration keys, plugin/mod APIs, mappings/loaders, Java requirements, proxy forwarding/authentication, and world/data formats.

## Artifact handling

- Download from the authoritative project release channel when possible.
- Verify published checksums/signatures if provided; otherwise record a local SHA-256 for traceability.
- Never execute artifacts from untrusted chat/file-sharing links without validation.
- Keep the previous known-good jar/plugin/mod/config available until verification completes.
- Do not overwrite the only copy of an existing artifact before rollback is secured.

Example local checksum:

```bash
sha256sum <artifact>
```

## Rollout sequence

1. freeze unrelated production changes;
2. capture baseline health and player load;
3. create/verify the required backup;
4. stage artifacts and config without activating them;
5. show the intended diff and versions;
6. drain or announce maintenance when disruption is expected;
7. stop the affected node gracefully if required;
8. atomically switch artifacts/config where practical;
9. start the node and tail logs from process start;
10. run smoke tests;
11. monitor a representative load window before broad rollout;
12. document outcome and retain rollback assets for an appropriate period.

For multi-node networks, prefer a canary backend or non-critical role before fleet-wide rollout when architecture allows it.

## Smoke tests

At minimum verify:

- process remains up without a restart loop;
- no new ERROR/FATAL pattern or repeating exception;
- expected port is listening and proxy routing succeeds;
- representative client can join;
- permissions/commands for key plugins still work;
- world/chunk load and save work;
- player/inventory/economy or other critical persistence works;
- TPS/MSPT, heap/GC, CPU, and latency are not materially regressed.

## Rollback

Rollback when success criteria fail and the cause is not a trivial, low-risk correction.

Rollback order:

1. stop writes cleanly;
2. restore prior artifacts/config;
3. restore data only if the deployment migrated or corrupted persistent state;
4. restart and verify against the pre-change baseline;
5. preserve failed-version logs and artifacts for diagnosis.

Never downgrade a world or database across an incompatible format boundary unless upstream explicitly supports it or a pre-upgrade backup is being restored.

## Java/runtime changes

Treat Java changes as independent deployments. Confirm the exact Java major version supported by the target server implementation and mods/plugins. Compare startup flags for compatibility; remove obsolete or unsupported JVM options instead of carrying them forward blindly.
