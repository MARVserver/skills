---
name: minecraft-plugin-testing-debugging
description: Test and debug Minecraft plugins with layered automated tests, isolated integration servers, reproducible fixtures, structured logging, stack-trace analysis, and regression verification.
---

# Minecraft Plugin Testing and Debugging

Use this skill for test strategy, bug reproduction, crash analysis, and release qualification.

## Test pyramid

- Unit-test domain logic, parsers, calculations, permissions, serializers, and migrations without a server when possible.
- Use API mocks only for narrow contracts; do not mistake mocked behavior for server compatibility.
- Run integration tests on an isolated server for commands, events, scheduler behavior, persistence, and plugin interoperability.
- Run smoke tests against every supported server/version family before release.

## Debugging workflow

1. capture exact server, plugin, Java, dependency, and configuration versions;
2. preserve the first relevant exception and full causal chain;
3. reduce to the smallest reproducible scenario;
4. separate plugin defect, platform defect, dependency conflict, configuration error, and bad data;
5. add temporary structured diagnostics around the suspected boundary;
6. fix the smallest supported cause;
7. add a regression test or reproducible fixture;
8. remove noisy diagnostics and verify clean startup/runtime logs.

## High-value cases

Test first install, upgrade, downgrade/rollback expectations, missing dependency, malformed config, unavailable database, duplicate events, player disconnect mid-operation, server shutdown during writes, permission denial, empty/full inventories, world unload, and concurrency races.

Never debug by repeatedly modifying the only production copy when a reproducible staging environment can be created.