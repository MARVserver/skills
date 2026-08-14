---
name: minecraft-server-operations
description: Safely operate production Minecraft Java Edition servers and proxies, including health checks, console actions, start/stop/restart, configuration changes, and routine maintenance.
---

# Minecraft Server Operations

Use this skill for day-to-day administration of Minecraft Java Edition servers or proxy nodes.

## Establish context first

Before changing anything, determine:

- server role: backend game server, lobby, proxy, or standalone;
- implementation and exact version: e.g. Paper/Purpur, Fabric/Forge/NeoForge, Velocity, or another implementation;
- Minecraft protocol/game version and Java runtime;
- launch mechanism: systemd, Docker/Compose, Kubernetes, game panel, tmux/screen, or direct process;
- server root, world directories, plugin/mod directories, and log location;
- whether players are online and whether maintenance was announced;
- current health: process state, joinability, TPS/MSPT when available, memory, CPU, disk free space, and recent errors.

Do not guess paths, service names, container names, ports, or credentials. Discover them from the host configuration.

## Routine workflow

1. **Observe.** Capture current status and the last relevant log lines before acting.
2. **Classify impact.** Decide whether the action is read-only, online-safe, disruptive, or destructive.
3. **Choose the graceful control path.** Prefer console/RCON or the service manager that owns the process.
4. **Execute the minimum change.** Avoid combining unrelated configuration or plugin changes.
5. **Verify.** Confirm process health, logs, port/listener state, player joinability, world persistence, and relevant metrics.
6. **Record.** Summarize what changed, why, commands/config touched, and rollback path.

## Health checks

Use the controls available on the host. Typical Linux checks include:

```bash
systemctl status <service> --no-pager
journalctl -u <service> -n 100 --no-pager
ps -ef | grep -E '[j]ava|[m]inecraft'
ss -lntp
df -h
df -i
free -h
```

For containers, inspect the orchestrator rather than treating the Java process as an unmanaged host process.

Useful Minecraft signals:

- successful startup/completion message;
- no repeating stack traces or restart loop;
- TPS close to 20 and MSPT below the 50 ms tick budget under normal load;
- no sustained GC pressure or host swapping;
- world files writable and adequate disk/inode headroom;
- expected proxy/backend routes reachable;
- representative player can connect, authenticate as expected, change dimensions, and interact with persistent data.

## Graceful restart

Before a planned restart:

1. announce maintenance if players are connected;
2. ensure no backup/restore, world conversion, pregeneration, or migration is in progress;
3. issue `save-all flush` through a trusted console path when supported;
4. request a normal server `stop`, or stop the owning service/container cleanly;
5. wait for shutdown completion and filesystem flush;
6. start through the same service manager;
7. watch logs through startup and perform post-start verification.

Avoid sending repeated stop/start requests. Do not use `kill -9` as a normal restart mechanism; it bypasses graceful shutdown and can increase corruption risk.

## Configuration changes

Before editing:

- confirm the active config file and whether the implementation rewrites it;
- back up the original file;
- check syntax/schema/version compatibility;
- understand whether reload is supported and safe. Prefer a restart when upstream documentation warns that reloads are partial or unsafe.

After editing, show a focused diff and validate only the intended keys changed.

## Console and RCON safety

- Never print RCON passwords or embed them in shell history when avoidable.
- Treat console commands as production mutations.
- Confirm selectors, player names, world names, coordinates, and destructive command scope before execution.
- Prefer reversible administrative actions over mass data edits.

## Stop conditions

Stop and escalate instead of continuing when:

- the world appears corrupt or a restore may be required;
- disk is full or the filesystem is read-only;
- the process repeatedly crashes after startup;
- an upgrade crossed an irreversible world/data format boundary without a verified backup;
- credentials or private keys may have been exposed;
- the requested action conflicts with the hosting/orchestration control plane.

Use the incident-response or backup-recovery skill for those cases.
