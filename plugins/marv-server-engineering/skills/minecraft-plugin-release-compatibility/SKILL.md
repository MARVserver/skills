---
name: minecraft-plugin-release-compatibility
description: Build, version, package, release, and maintain Minecraft plugins with reproducible artifacts, compatibility matrices, changelogs, migration notes, CI checks, and rollback-ready releases.
---

# Minecraft Plugin Release and Compatibility

Use this skill for CI/CD, version support, publishing, upgrade guidance, and deprecation.

## Release contract

Every release should identify plugin version, commit, build environment, required Java version, supported server/API versions, required/optional dependencies, data migration impact, and known incompatibilities.

## Pipeline

1. run formatting/static analysis and tests;
2. build from a clean checkout;
3. verify dependency locking/resolution and artifact contents;
4. run integration smoke tests on representative supported targets;
5. generate checksum and changelog;
6. test upgrade from the previous supported release;
7. document backup and rollback requirements;
8. publish the immutable artifact and release notes.

## Compatibility discipline

Do not claim compatibility from compilation alone. Verify startup, commands, events, persistence, protocol/platform-specific behavior, and integrations on actual target environments. Isolate version-specific adapters and remove a support target deliberately with documented migration guidance.

Data format changes must have explicit migration versions and must not silently make rollback impossible.