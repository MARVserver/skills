# Releasing MARV Server Engineering for Minecraft

This repository publishes `marv-server-engineering` as a versioned Codex/OpenAI plugin bundle.

## Release contract

A release tag must be `v<version>` where `<version>` exactly matches the `version` field in:

`plugins/marv-server-engineering/.codex-plugin/plugin.json`

For example, manifest version `0.2.0` must be released from tag `v0.2.0`.

## Before tagging

1. Update the plugin manifest version when preparing a new release.
2. Update `plugins/marv-server-engineering/submission/RELEASE_NOTES.md`.
3. Run:

   ```bash
   python3 scripts/validate_plugin.py
   python3 scripts/validate_plugin.py --check-urls
   ```

4. Merge the release-preparation PR only after `Validate Plugin` succeeds.
5. Confirm the release commit on `main` is the exact commit intended for distribution.

## Create the release

Create and push an annotated tag from the intended `main` commit:

```bash
git switch main
git pull --ff-only
git tag -a v0.2.0 -m "MARV Server Engineering v0.2.0"
git push origin v0.2.0
```

Pushing a `v*.*.*` tag starts `.github/workflows/release-plugin.yml`.

The workflow:

1. verifies the tag matches the manifest version;
2. runs the full plugin validator, including public URL checks;
3. builds `marv-server-engineering-vX.Y.Z.zip`;
4. generates a SHA-256 checksum file;
5. creates the GitHub Release and uploads both files.

The release fails instead of publishing if version/tag validation or package validation fails.

## After publishing

- Verify the GitHub Release points at the intended tag and commit.
- Download the ZIP and verify its SHA-256 against the uploaded checksum.
- Confirm the archive contains `plugins/marv-server-engineering/.codex-plugin/plugin.json` and all 32 `SKILL.md` files.
- Re-run a clean Codex installation from the public marketplace source:

  ```bash
  codex plugin marketplace add MARVserver/skills
  codex plugin add marv-server-engineering@marvserver
  codex plugin list
  ```

- Start a new Codex thread and run the smoke-test prompts in `plugins/marv-server-engineering/submission/TEST_CASES.md`.

## Branding gate

The current website favicon is only 16×16 pixels and is not suitable as the primary public listing logo. Do not upscale it and present it as a high-resolution brand asset. Add a publisher-approved MARVserver-owned square logo before any directory surface that requires one.

Do not use Minecraft, Mojang, or Microsoft official artwork or logos as the plugin logo.
