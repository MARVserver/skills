#!/usr/bin/env python3
"""Validate the MARV Server Engineering Codex plugin distribution package."""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

PLUGIN_ID = "marv-server-engineering"
MARKETPLACE_ID = "marvserver"
EXPECTED_SKILL_COUNT = 32  # 31 domain skills + index router
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
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing required JSON file: {path}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path}: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"expected JSON object in {path}")
        return {}
    return data


def require_file(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing required file: {path}")
        return ""


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def safe_child(base: Path, relative: str) -> Path | None:
    candidate = (base / relative).resolve()
    try:
        candidate.relative_to(base.resolve())
    except ValueError:
        return None
    return candidate


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing skill file: {path}")
        return {}

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{path}: YAML front matter must start with ---")
        return {}

    try:
        closing = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        errors.append(f"{path}: YAML front matter has no closing ---")
        return {}

    fields: dict[str, str] = {}
    for lineno, raw in enumerate(lines[1:closing], start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1].isspace():
            errors.append(f"{path}:{lineno}: nested YAML is not expected in skill front matter")
            continue
        if ":" not in raw:
            errors.append(f"{path}:{lineno}: expected key: value front-matter entry")
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in fields:
            errors.append(f"{path}:{lineno}: duplicate front-matter key {key!r}")
        fields[key] = value

    for required in ("name", "description"):
        if not fields.get(required):
            errors.append(f"{path}: front matter requires non-empty {required!r}")
    return fields


def validate_package(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []

    plugin_dir = root / "plugins" / PLUGIN_ID
    manifest_path = plugin_dir / ".codex-plugin" / "plugin.json"
    marketplace_path = root / ".agents" / "plugins" / "marketplace.json"
    privacy_path = root / "PRIVACY.md"
    support_path = root / "SUPPORT.md"
    notice_path = plugin_dir / "NOTICE.md"
    readme_path = root / "README.md"

    manifest = load_json(manifest_path, errors)
    marketplace = load_json(marketplace_path, errors)

    if manifest:
        if manifest.get("name") != PLUGIN_ID:
            errors.append(f"manifest name must be {PLUGIN_ID!r}")
        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
            errors.append("manifest version must be valid semantic versioning")
        if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
            errors.append("manifest description must be non-empty")
        if manifest.get("license") != "MIT":
            errors.append("manifest license must remain MIT")
        if manifest.get("repository") != "https://github.com/MARVserver/skills":
            errors.append("manifest repository must point to MARVserver/skills")
        if "apps" in manifest or "mcpServers" in manifest:
            errors.append("version 0.2.x is skills-only; apps/mcpServers must not be declared")

        skills_ref = manifest.get("skills")
        if skills_ref != "./skills/":
            errors.append("manifest skills must be exactly './skills/'")
        elif safe_child(plugin_dir, skills_ref) != (plugin_dir / "skills").resolve():
            errors.append("manifest skills path escapes or does not resolve to plugin skills directory")

        interface = manifest.get("interface")
        if not isinstance(interface, dict):
            errors.append("manifest interface must be an object")
            interface = {}
        if interface.get("displayName") != "MARV Server Engineering for Minecraft":
            errors.append("manifest displayName does not match the public plugin name")
        if interface.get("developerName") != "MARVserver":
            errors.append("manifest developerName must be MARVserver")
        if interface.get("category") != "Developer Tools":
            errors.append("manifest category must be Developer Tools")
        if DISCLAIMER not in str(interface.get("longDescription", "")):
            errors.append("manifest longDescription must contain the Minecraft non-affiliation notice")
        prompts = interface.get("defaultPrompt")
        if not isinstance(prompts, list) or len(prompts) < 3 or not all(isinstance(x, str) and x.strip() for x in prompts):
            errors.append("manifest defaultPrompt must contain at least three non-empty prompts")

        for key in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
            if not is_https_url(interface.get(key)):
                errors.append(f"manifest interface.{key} must be a public HTTPS URL")
        expected_privacy = "https://github.com/MARVserver/skills/blob/main/PRIVACY.md"
        if interface.get("privacyPolicyURL") != expected_privacy:
            errors.append(f"manifest privacyPolicyURL must be {expected_privacy}")

    if marketplace:
        if marketplace.get("name") != MARKETPLACE_ID:
            errors.append(f"marketplace name must be {MARKETPLACE_ID!r}")
        entries = marketplace.get("plugins")
        if not isinstance(entries, list):
            errors.append("marketplace plugins must be an array")
            entries = []
        matches = [entry for entry in entries if isinstance(entry, dict) and entry.get("name") == PLUGIN_ID]
        if len(matches) != 1:
            errors.append(f"marketplace must contain exactly one {PLUGIN_ID!r} entry")
        else:
            entry = matches[0]
            source = entry.get("source")
            if not isinstance(source, dict):
                errors.append("marketplace plugin source must be an object")
                source = {}
            if source.get("source") != "local":
                errors.append("marketplace plugin source.source must be 'local'")
            source_path = source.get("path")
            if source_path != f"./plugins/{PLUGIN_ID}":
                errors.append(f"marketplace plugin source.path must be './plugins/{PLUGIN_ID}'")
            elif safe_child(root, source_path) != plugin_dir.resolve():
                errors.append("marketplace source.path does not resolve to the plugin directory")

            policy = entry.get("policy")
            if not isinstance(policy, dict):
                errors.append("marketplace plugin policy must be an object")
                policy = {}
            if policy.get("installation") != "AVAILABLE":
                errors.append("marketplace installation policy must be AVAILABLE")
            if policy.get("authentication") != "ON_INSTALL":
                errors.append("marketplace authentication policy must be ON_INSTALL")
            if entry.get("category") != "Developer Tools":
                errors.append("marketplace category must be Developer Tools")

    privacy_text = require_file(privacy_path, errors)
    support_text = require_file(support_path, errors)
    notice_text = require_file(notice_path, errors)
    readme_text = require_file(readme_path, errors)

    if privacy_text and "MARV Server Engineering for Minecraft" not in privacy_text:
        errors.append("PRIVACY.md must identify the plugin it covers")
    if support_text:
        if "https://github.com/MARVserver/skills/issues" not in support_text:
            errors.append("SUPPORT.md must link to the public GitHub Issues page")
        if "marvsystem@gmail.com" not in support_text:
            errors.append("SUPPORT.md must include the publisher support email")
    for path, text in ((notice_path, notice_text), (readme_path, readme_text)):
        if text and DISCLAIMER not in text:
            errors.append(f"{path}: missing Minecraft non-affiliation notice")

    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        errors.append(f"missing skills directory: {skills_dir}")
        skill_files: list[Path] = []
    else:
        skill_files = sorted(skills_dir.glob("*/SKILL.md"))
        skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
        missing_skill_docs = [p.name for p in skill_dirs if not (p / "SKILL.md").is_file()]
        if missing_skill_docs:
            errors.append("skill directories missing SKILL.md: " + ", ".join(missing_skill_docs))

    if len(skill_files) != EXPECTED_SKILL_COUNT:
        errors.append(
            f"expected {EXPECTED_SKILL_COUNT} bundled skills (31 domain + index), found {len(skill_files)}"
        )

    names: set[str] = set()
    for skill_file in skill_files:
        fields = parse_frontmatter(skill_file, errors)
        name = fields.get("name", "")
        folder = skill_file.parent.name
        if name and name != folder:
            errors.append(f"{skill_file}: front-matter name {name!r} must match folder {folder!r}")
        if name and not SKILL_NAME_RE.fullmatch(name):
            errors.append(f"{skill_file}: invalid skill name {name!r}; use lower-case hyphen-case")
        if name in names:
            errors.append(f"duplicate skill name: {name}")
        elif name:
            names.add(name)

    if "index" not in names:
        errors.append("router skill 'index' is required")
    domain_count = len(names - {"index"})
    if names and domain_count != 31:
        errors.append(f"expected 31 domain skills plus index, found {domain_count} domain skills")

    if not errors:
        notes.append(f"manifest: {manifest.get('name')} {manifest.get('version')}")
        notes.append(f"marketplace: {marketplace.get('name')}")
        notes.append(f"skills: {len(skill_files)} total ({domain_count} domain + index)")
        notes.append("public policy/support and trademark notice: present")
    return errors, notes


def public_urls(root: Path) -> list[str]:
    errors: list[str] = []
    manifest = load_json(root / "plugins" / PLUGIN_ID / ".codex-plugin" / "plugin.json", errors)
    if errors or not manifest:
        return []
    interface = manifest.get("interface", {}) if isinstance(manifest.get("interface"), dict) else {}
    urls = [
        manifest.get("repository"),
        manifest.get("homepage"),
        interface.get("websiteURL"),
        interface.get("privacyPolicyURL"),
        interface.get("termsOfServiceURL"),
        "https://github.com/MARVserver/skills/issues",
    ]
    return list(dict.fromkeys(url for url in urls if isinstance(url, str) and url))


def check_url(url: str, attempts: int = 3, timeout: int = 15) -> str | None:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MARVserver-plugin-validator/1.0",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        },
        method="GET",
    )
    last_error = "unknown error"
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = getattr(response, "status", 200)
                response.read(1)
                if 200 <= status < 400:
                    return None
                last_error = f"HTTP {status}"
        except urllib.error.HTTPError as exc:
            last_error = f"HTTP {exc.code}"
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
        if attempt < attempts:
            time.sleep(attempt * 2)
    return f"{url}: unavailable after {attempts} attempts ({last_error})"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of scripts/)",
    )
    parser.add_argument(
        "--check-urls",
        action="store_true",
        help="also verify public repository, policy, support, and publisher URLs",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    errors, notes = validate_package(root)
    for note in notes:
        print(f"OK: {note}")

    if args.check_urls and not errors:
        urls = public_urls(root)
        print(f"Checking {len(urls)} public URLs...")
        for url in urls:
            problem = check_url(url)
            if problem:
                errors.append(problem)
            else:
                print(f"OK: {url}")

    if errors:
        print("\nPlugin validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("\nPlugin validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
