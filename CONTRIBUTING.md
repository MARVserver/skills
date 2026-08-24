# Contributing to MARVserver Minecraft Skills

Thanks for helping improve the skill pack. Contributions should make the skills more accurate, safer, easier to apply, or easier to maintain.

## Before you start

Use the right channel for the work:

- **Bug or incorrect behavior:** open an issue with the bug report form.
- **New skill or significant capability:** start in GitHub Discussions under **Ideas** before investing in a large change.
- **How-to or usage question:** use GitHub Discussions under **Q&A**.
- **Security vulnerability:** follow `SECURITY.md`; do not open a public issue.

Small documentation fixes can go directly to a pull request.

## Repository conventions

The primary plugin lives under:

```text
plugins/marv-server-engineering/
```

Skills live at:

```text
plugins/marv-server-engineering/skills/<skill-name>/SKILL.md
```

Keep skill names lowercase and hyphen-separated. Prefer focused skills with a clear operational boundary over broad catch-all instructions.

## Skill quality requirements

A contribution should:

1. State clearly when the skill should be used.
2. Use version-aware guidance when Minecraft, Java, server software, APIs, or tooling differ by version.
3. Prefer least privilege and reversible changes.
4. Require backup or rollback planning before destructive operations.
5. Separate observations from assumptions during debugging.
6. Avoid unnecessary collection or exposure of player data, credentials, tokens, or infrastructure secrets.
7. Include concrete verification steps after operational changes.
8. Avoid inventing commands, configuration keys, APIs, or compatibility claims.

## Local validation

Run:

```bash
python3 scripts/validate_plugin.py
```

Fix validation errors before opening a pull request.

## Pull requests

Keep each pull request focused. In the description, explain:

- what changed;
- why it is needed;
- which skills or files are affected;
- how you validated the change;
- any compatibility, security, or operational risk.

Reviewers may ask for narrower scope, stronger validation, clearer rollback guidance, or source verification for version-sensitive claims.

## Community standards

Participation in this repository is governed by `CODE_OF_CONDUCT.md`. Support routing is described in `SUPPORT.md`.
