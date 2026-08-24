# Skill authoring

Use this guide when adding a skill or materially changing an existing one.

## Location and naming

Skills live under:

```text
plugins/marv-server-engineering/skills/<skill-name>/SKILL.md
```

Use lowercase, hyphen-separated names. Keep each skill focused on a coherent engineering or operations domain.

## Design requirements

A strong skill should make the following explicit:

1. **Trigger:** when the skill is appropriate and when another skill is a better fit.
2. **Inputs:** information needed before making a recommendation or operational change.
3. **Version assumptions:** Minecraft, Java, server/proxy, mod-loader, plugin, API, or tool versions that affect the answer.
4. **Safety boundaries:** destructive operations, permissions, credentials, player data, and production impact.
5. **Execution order:** prerequisite checks before commands or configuration changes.
6. **Verification:** how to prove that the change worked.
7. **Rollback:** how to recover when the change fails or causes regression.

## Reliability expectations

Do not invent commands, configuration keys, APIs, compatibility claims, or version behavior. When behavior is version-sensitive, require verification against current upstream documentation or release notes.

Operational guidance should prefer reversible changes and least privilege. Backups should be verified rather than merely assumed to exist.

## Privacy and security

Avoid requesting or reproducing unnecessary:

- access tokens and API keys;
- passwords or session secrets;
- private IP addresses or internal topology;
- database dumps;
- personally identifying player data.

When evidence is needed, ask for the minimum sanitized excerpt that can answer the question.

## Validation

Run:

```bash
python3 scripts/validate_plugin.py
```

Then review the affected skill manually for routing clarity, unsafe assumptions, inconsistent terminology, stale versions, and missing verification or rollback steps.

## Pull request scope

Prefer one coherent change per pull request. If a proposal changes the skill taxonomy or adds a large new capability, discuss it under the **Ideas** category before implementation.
