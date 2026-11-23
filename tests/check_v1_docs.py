"""Check V1.0 documentation consistency without loading or running the Skill."""

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/council-designer/SKILL.md"
GUIDE = SKILL.with_name("README.md")
MODES = ("Design", "Review", "Update", "Export")
MARKERS = ("❓", "🧭", "🔍", "➜", "✅")
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^()\s]+)\)")


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def text(path):
    return path.read_text(encoding="utf-8")


def markdown_links(source):
    prose = re.sub(r"^\x60{3}[^\n]*\n.*?^\x60{3}[ \t]*$", "", source, flags=re.M | re.S)
    return LINK.findall(prose)


def check_skill():
    frontmatter = re.match(r"\A---\n(.+?)\n---\n(.+)\Z", text(SKILL), re.S)
    require(frontmatter is not None, "SKILL.md needs frontmatter followed by Markdown")
    header, body = frontmatter.groups()
    name = re.search(r"^name: ([-a-z0-9]{1,64})$", header, re.M)
    description = re.search(r"^description: ([^\n]+)$", header, re.M)
    require(name and name[1] == SKILL.parent.name, "Invalid or mismatched skill name")
    require(description and len(description[1]) <= 1024, "Invalid skill description")
    version = re.search(r'^metadata:\n  version: "(\d+\.\d+\.\d+)"$', header, re.M)
    require(version and version[1] == "1.0.0", "Expected version 1.0.0 under metadata")
    fields = set(re.findall(r"^([a-z-]+):", header, re.M))
    require(fields == {"name", "description", "metadata"}, "Unexpected skill metadata fields")
    require(not markdown_links(body), "The standalone instructions must carry their own context")
    require(
        tuple(re.findall(r"^### (Design|Review|Update|Export)$", body, re.M)) == MODES,
        "The expected four modes are missing or out of order",
    )
    guide = text(GUIDE)
    require("v" + version[1] in guide, "Skill guide version differs from metadata")
    require(
        tuple(re.findall(r"^\| (Design|Review|Update|Export) \|", guide, re.M)) == MODES,
        "Skill and guide modes differ",
    )
    for document_name, document in (("Skill", body), ("guide", guide)):
        table_markers = re.findall(r"^\| (❓|🧭|🔍|➜|✅) \|", document, re.M)
        require(
            tuple(table_markers) == MARKERS,
            document_name + " marker table does not match the five literal markers",
        )
    return len(body.splitlines())


def check_readmes_and_ledger():
    en, zh = (text(ROOT / name) for name in ("README.md", "README.zh-CN.md"))
    require(markdown_links(en) == markdown_links(zh), "Bilingual README navigation differs")
    for document in (en, zh):
        require(all(mode in document for mode in MODES), "README does not name all four modes")
        require("v1.0.0" in document, "README version differs from the Skill")
    scenario_path = ROOT / "tests/V1-ACCEPTANCE-TESTS.md"
    scenarios = re.findall(r"^## (V1-\d{2}) — ", text(scenario_path), re.M)
    ledger = re.findall(
        r"^\| (V1-\d{2}) \| [^|]+ \| ([^|]+) \|$",
        text(ROOT / "tests/V1-TEST-RESULTS.md"),
        re.M,
    )
    require(len(set(scenarios)) == len(scenarios) == 9, "Duplicate or missing scenario IDs")
    require(scenarios == [case for case, _ in ledger], "Scenario and ledger IDs differ")
    statuses = {status for _, status in ledger}
    require(statuses <= {"Not Run", "Passed", "Partial", "Failed", "Blocked"}, "Invalid status")
    if statuses == {"Not Run"}:
        require("Not Run" in en and "Not Run" in zh, "READMEs must disclose unrun behavior")
    return len(scenarios)


def check_links():
    checked = 0
    for file in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in file.relative_to(ROOT).parts):
            continue
        for link in markdown_links(text(file)):
            target = urlsplit(link)
            if target.scheme or target.netloc or not target.path:
                continue
            resolved = (file.parent / unquote(target.path)).resolve()
            require(resolved.is_relative_to(ROOT) and resolved.exists(), f"{file}: missing {link}")
            checked += 1
    return checked


if __name__ == "__main__":
    print(f"PASS: metadata, standalone instructions, modes and markers ({check_skill()} body lines)")
    print(f"PASS: bilingual README navigation and {check_readmes_and_ledger()} paired scenario IDs")
    print(f"PASS: {check_links()} local Markdown link targets")
