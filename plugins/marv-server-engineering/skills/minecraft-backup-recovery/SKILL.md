---
name: minecraft-backup-recovery
description: Design, run, verify, and restore Minecraft server backups with consistency controls, retention, off-host copies, restore drills, and disaster-recovery procedures.
---

# Minecraft Backup and Recovery

Use this skill before risky changes and for routine backup, restore, migration, or disaster recovery.

## Define what must be recoverable

Inventory persistent state, including:

- all active worlds/dimensions;
- server and proxy configuration;
- plugins/mods and their data directories;
- permissions, bans, whitelist, ops, advancements/statistics/playerdata;
- maps, scripts, datapacks/resource packs when locally hosted;
- embedded databases (SQLite/H2/etc.);
- external databases/caches where they contain authoritative game state;
- secrets needed for recovery, stored separately and securely;
- service/container/orchestration definitions and launch parameters.

A world-only backup is not necessarily a server recovery backup.

## Consistency modes

### Cold backup — preferred for highest consistency

1. announce maintenance;
2. issue `save-all flush` when supported;
3. stop the server gracefully;
4. wait for process exit and filesystem flush;
5. snapshot/copy the persistent state;
6. restart and verify.

### Coordinated hot backup

Use only when downtime requirements justify it and the server/filesystem strategy is understood.

1. trigger a full save/flush;
2. temporarily coordinate autosave behavior only if the implementation and procedure explicitly support it;
3. take an atomic filesystem/storage snapshot as quickly as possible;
4. immediately restore normal save behavior;
5. copy/export from the snapshot, not from a continuously mutating live tree.

Do not leave autosave disabled after an error path. Prefer a cold backup over an improvised live `tar` of actively changing world files.

## External databases

Filesystem copies of a live external database are not automatically consistent. Use the database's supported snapshot/dump mechanism or storage-level consistency procedure. Coordinate the recovery point with world/plugin state when cross-system consistency matters.

## Backup verification

A backup is not successful merely because a file exists. Verify:

- job exit status;
- archive/object size is plausible versus recent history;
- expected world/config/database objects are present;
- checksum/integrity test passes where available;
- encryption keys are accessible through the recovery process;
- retention/off-host replication completed;
- restore test succeeds on an isolated environment.

Maintain RPO/RTO targets appropriate to the server and test that the backup design can meet them.

## Retention

Use multiple generations and at least one failure-domain-separated copy. A practical design may include frequent local snapshots plus less frequent off-host/object-storage copies with longer retention.

Do not let automated retention delete the only known-good pre-upgrade backup until the upgrade is proven stable and rollback is no longer required.

## Restore procedure

1. define the exact recovery point and scope;
2. stop or isolate production to prevent new writes;
3. preserve the broken/current state for forensic recovery when feasible;
4. validate backup integrity before overwriting production;
5. restore to a staging path/environment first when time permits;
6. restore worlds, plugin/mod data, config, and databases consistently;
7. verify ownership/permissions and launch configuration;
8. start in a controlled manner and inspect logs;
9. test join, world load/save, dimensions, inventory/player data, permissions, and critical plugin persistence;
10. reopen traffic only after verification.

Never restore an untrusted archive as a privileged user without checking paths/symlinks and archive contents.

## Restore drill output

Record:

```text
backup timestamp / recovery point
backup source and checksum/integrity result
data sets restored
restore duration
verification results
measured RPO
measured RTO
issues and remediation
```
