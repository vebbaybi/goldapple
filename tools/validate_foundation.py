"""Dependency-free structural validation for the Phase 0 repository."""
from __future__ import annotations
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

required = [
    "README.md", "VISION.md", "PRODUCT_PRINCIPLES.md", "ROADMAP.md", "GLOSSARY.md",
    "WHITEPAPER.md", "AGENTS.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
    "CHANGELOG.md", "docs/audits/FOUNDATION_AUDIT.md", "docs/TRACEABILITY_MATRIX.md",
    "gaxyz/index.html", "gaxyz/styles.css", "gaxyz/script.js", "gaxyz/README.md",
    "gaxyz/SITE_ARCHITECTURE.md", "gaxyz/CONTENT_MAP.md",
    "gaxyz/CONTENT_SOURCE_POLICY.md", "gaxyz/STATUS_MAPPING.md",
]
for item in required:
    if not (ROOT / item).is_file(): errors.append(f"missing required file: {item}")

link_pattern = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
for doc in ROOT.rglob("*.md"):
    if ".git" in doc.parts: continue
    text = doc.read_text(encoding="utf-8")
    for target in link_pattern.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"): continue
        path = (doc.parent / unquote(target)).resolve()
        if not path.exists(): errors.append(f"broken link: {doc.relative_to(ROOT)} -> {target}")

id_pattern = re.compile(r"\bGA-(?:FR|NFR|SEC|PRIV|US|SCN)-\d{3}\b")
definitions: dict[str, str] = {}
for doc in (ROOT / "docs").rglob("*.md"):
    for line in doc.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"): continue
        ids = id_pattern.findall(line)
        if not ids: continue
        first = ids[0]
        # Traceability references are uses, not definitions.
        if doc.name == "TRACEABILITY_MATRIX.md": continue
        if first in definitions: errors.append(f"duplicate ID {first}: {definitions[first]} and {doc.relative_to(ROOT)}")
        else: definitions[first] = str(doc.relative_to(ROOT))

for forbidden in [".github/workflows/pages.yml", "netlify.toml", "vercel.json"]:
    if (ROOT / forbidden).exists(): errors.append(f"unexpected deployment configuration: {forbidden}")

html = (ROOT / "gaxyz/index.html").read_text(encoding="utf-8")
for target in re.findall(r"(?:src|href)=\"([^\"]+)\"", html):
    if target.startswith(("http", "#")): continue
    path = ((ROOT / "gaxyz") / target.split("#", 1)[0]).resolve()
    if not path.exists(): errors.append(f"broken HTML asset/link: {target}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)
print(f"VALIDATION OK: {len(required)} required files, {len(definitions)} unique defined IDs, Markdown and HTML local links resolved")
