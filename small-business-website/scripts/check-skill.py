#!/usr/bin/env python3
"""Validate the small-business-website skill. Run: python3 check-skill.py"""
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
errors = []

if not skill.exists():
    print("FAIL: SKILL.md missing")
    sys.exit(1)

text = skill.read_text(encoding="utf-8")
lines = text.splitlines()

# Frontmatter must be first line
if not text.startswith("---\n"):
    errors.append("frontmatter must start on the very first line")
parts = text.split("---\n", 2)
if len(parts) < 3:
    errors.append("frontmatter block not found (needs opening and closing ---)")
    print("\n".join(errors))
    sys.exit(1)
front = parts[1]

name_m = re.search(r"^name:\s*(.+)$", front, re.M)
desc_m = re.search(r"^description:\s*(.+)$", front, re.M)
if not name_m:
    errors.append("frontmatter: name missing")
else:
    name = name_m.group(1).strip()
    if name != "small-business-website":
        errors.append(f"frontmatter: name is {name!r}, expected 'small-business-website'")
    if len(name) > 64 or not re.fullmatch(r"[a-z0-9-]+", name):
        errors.append("frontmatter: name must be <=64 chars, lowercase letters, numbers, hyphens only")
    if "claude" in name or "anthropic" in name:
        errors.append("frontmatter: name must not contain 'claude' or 'anthropic'")
if not desc_m:
    errors.append("frontmatter: description missing")
else:
    desc = desc_m.group(1).strip()
    if len(desc) > 1024:
        errors.append(f"frontmatter: description is {len(desc)} chars, max 1024")
    if "<" in desc or ">" in desc:
        errors.append("frontmatter: description must not contain angle brackets")
    if "when" not in desc.lower() and "use when" not in desc.lower():
        errors.append("frontmatter: description should state when to use it")

if len(lines) >= 500:
    errors.append(f"SKILL.md is {len(lines)} lines, must be under 500")

for ref in ["references/brief.md", "references/design.md",
            "references/booking-quote.md", "references/seo-deploy.md",
            "examples/barbershop.md", "examples/cleaning-quote.md"]:
    if not (root / ref).exists():
        errors.append(f"missing referenced file: {ref}")

# No Nigeria-specific content in the skill itself
for bad in ["Nigeria", "Nigerian", "Naira", "Lagos", "Abuja"]:
    if bad in text:
        errors.append(f"SKILL.md must not contain Nigeria-specific content: found {bad!r}")

print(f"SKILL.md: {len(lines)} lines")
if desc_m:
    print(f"description: {len(desc_m.group(1).strip())} chars")
print(f"references checked: 6 files")
if errors:
    print("FAIL:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("PASS: skill is valid")
