#!/usr/bin/env python3
"""Validate the MARVserver Minecraft skill pack."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PLUGIN_ID = "marv-server-engineering"
MARKETPLACE_ID = "marvserver"
EXPECTED_SKILL_COUNT = 32  # 31 specialist skills + index router
DISCLAIMER = (
    "NOT AN OFFICIAL MINECRAFT PRODUCT. "
    "NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT."
)
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing required file: {path}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"expected JSON object in {path}")
        return {}
    return value


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing required file: {path}")
        return ""


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = read_text(path, errors)
    if not text:
        return {}

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{path}: front matter must start with ---")
        return {}

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        errors.append(f"{path}: front matter is not closed with ---")
        return {}

    result: dict[str, str] = {}
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            errors.append(f"{path}: unsupported front matter line: {stripped}")
            continue
        key, value = stripped.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    plugin_root = root / "plugins" / PLUGIN_ID
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    marketplace_path = root / ".agents" / "plugins" / "marketplace.json"
    skills_root = plugin_root / "skills"
    errors: list[str] = []

    manifest = load_json(manifest_path, errors)
    marketplace = load_json(marketplace_path, errors)

    if manifest:
        if manifest.get("name") != PLUGIN_ID:
            errors.append(f"manifest name must be {PLUGIN_ID!r}")
        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
            errors.append("manifest version must be valid semantic versioning")
        if manifest.get("skills") != "./skills/":
            errors.append('manifest skills must be "./skills/"')
        if manifest.get("repository") != "https://github.com/MARVserver/skills":
            errors.append("manifest repository must point to MARVserver/skills")
        if manifest.get("license") != "MIT":
            errors.append("manifest license must be MIT")
        if "apps" in manifest or "mcpServers" in manifest:
            errors.append("this package is skills-only; apps/mcpServers must not be declared")

        interface = manifest.get("interface")
        if not isinstance(interface, dict):
            errors.append("manifest interface must be an object")
        else:
            for key in (
                "displayName",
                "shortDescription",
                "longDescription",
                "developerName",
                "category",
            ):
                if not isinstance(interface.get(key), str) or not interface[key].strip():
                    errors.append(f"manifest interface.{key} must be a non-empty string")
            if DISCLAIMER not in str(interface.get("longDescription", "")):
                errors.append("manifest longDescription must contain the Minecraft disclaimer")

    if marketplace:
        if marketplace.get("name") != MARKETPLACE_ID:
            errors.append(f"marketplace name must be {MARKETPLACE_ID!r}")
        entries = marketplace.get("plugins")
        if not isinstance(entries, list):
            errors.append("marketplace plugins must be an array")
        else:
            matches = [entry for entry in entries if isinstance(entry, dict) and entry.get("name") == PLUGIN_ID]
            if len(matches) != 1:
                errors.append(f"marketplace must contain exactly one {PLUGIN_ID!r} entry")
            else:
                entry = matches[0]
                source = entry.get("source")
                if source != {"source": "local", "path": f"./plugins/{PLUGIN_ID}"}:
                    errors.append("marketplace source must point to the local plugin directory")
                policy = entry.get("policy")
                if not isinstance(policy, dict):
                    errors.append("marketplace policy must be an object")
                else:
                    if policy.get("installation") != "AVAILABLE":
                        errors.append("marketplace installation policy must be AVAILABLE")
                    if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                        errors.append("marketplace authentication policy must be ON_INSTALL or ON_USE")

    if not skills_root.is_dir():
        errors.append(f"missing skills directory: {skills_root}")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())

    if len(skill_dirs) != EXPECTED_SKILL_COUNT:
        errors.append(
            f"expected {EXPECTED_SKILL_COUNT} skill directories, found {len(skill_dirs)}"
        )

    names: set[str] = set()
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        frontmatter = parse_frontmatter(skill_file, errors)
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        if not name:
            errors.append(f"{skill_file}: missing name")
        elif not SKILL_NAME_RE.fullmatch(name):
            errors.append(f"{skill_file}: invalid skill name {name!r}")
        elif name != skill_dir.name:
            errors.append(
                f"{skill_file}: front matter name {name!r} must match folder {skill_dir.name!r}"
            )
        elif name in names:
            errors.append(f"duplicate skill name: {name}")
        else:
            names.add(name)

        if not description:
            errors.append(f"{skill_file}: missing description")

    if "index" not in names:
        errors.append("index router skill is required")

    readme = read_text(root / "README.md", errors)
    install_command = (
        "codex plugin marketplace add MARVserver/skills && "
        "codex plugin add marv-server-engineering@marvserver"
    )
    if install_command not in readme:
        errors.append("README must contain the copy-paste installation command")
    if DISCLAIMER not in readme:
        errors.append("README must contain the Minecraft disclaimer")

    notice = read_text(plugin_root / "NOTICE.md", errors)
    if DISCLAIMER not in notice:
        errors.append("NOTICE.md must contain the Minecraft disclaimer")

    if errors:
        print("Skill pack validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"OK: {PLUGIN_ID} {manifest.get('version', '?')} — "
        f"{len(skill_dirs)} skills validated"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
