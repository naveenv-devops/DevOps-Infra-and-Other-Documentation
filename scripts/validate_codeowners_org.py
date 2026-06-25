#!/usr/bin/env python3
"""Read-only validation of .github/CODEOWNERS across org repositories."""

from __future__ import annotations

import base64
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ORG = "metapercept-metr"
TARGET_BRANCHES = ("dev", "devops-testing", "main")
CODEOWNERS_PATH = ".github/CODEOWNERS"
CODEOWNERS_HEADER = """# This is a basic CODEOWNERS file.
# See https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners for details on how to specify code owners.
"""
STANDARD_RULE = "*  @nilesh-sk @naveenv-devops"
RESTRICTED_RULE = "*  @naveenv-devops"
REQUIRED_OWNER = "naveenv-devops"


@dataclass
class Finding:
    repo: str
    branch: str
    status: str
    template: str
    issues: list[str]

    @property
    def invalid(self) -> bool:
        return self.status != "valid"


def gh_api(method: str, endpoint: str) -> object | None:
    proc = subprocess.run(
        ["gh", "api", "-X", method, endpoint],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        stderr = proc.stderr or ""
        if "404" in stderr:
            return None
        raise subprocess.CalledProcessError(
            proc.returncode,
            ["gh", "api", endpoint],
            output=proc.stdout,
            stderr=proc.stderr,
        )
    if not proc.stdout.strip():
        return None
    return json.loads(proc.stdout)


def list_repos() -> list[str]:
    proc = subprocess.run(
        ["gh", "api", f"orgs/{ORG}/repos?per_page=100", "--paginate"],
        check=True,
        capture_output=True,
        text=True,
    )
    repos: list[str] = []
    for chunk in proc.stdout.strip().split("\n\n"):
        chunk = chunk.strip()
        if not chunk:
            continue
        batch = json.loads(chunk)
        if isinstance(batch, list):
            repos.extend(r["name"] for r in batch)
    return sorted(set(repos))


def branch_exists(repo: str, branch: str) -> bool:
    return gh_api("GET", f"repos/{ORG}/{repo}/branches/{branch}") is not None


def fetch_codeowners_content(repo: str, branch: str) -> tuple[str | None, str | None]:
    for path in (CODEOWNERS_PATH, "CODEOWNERS"):
        data = gh_api("GET", f"repos/{ORG}/{repo}/contents/{path}?ref={branch}")
        if data and isinstance(data, dict) and data.get("content"):
            raw = base64.b64decode(data["content"]).decode("utf-8")
            return raw, path
    return None, None


def normalize_content(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines) + "\n"


def extract_owners(text: str) -> set[str]:
    owners: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        owners.update(re.findall(r"@([A-Za-z0-9_.-]+)", stripped))
    return owners


def github_syntax_errors(repo: str, branch: str) -> list[str]:
    data = gh_api("GET", f"repos/{ORG}/{repo}/codeowners/errors?ref={branch}")
    if not data or not isinstance(data, dict):
        return []
    errors = data.get("errors") or []
    messages: list[str] = []
    for err in errors:
        line = err.get("line", "?")
        message = err.get("message", "syntax error")
        path = err.get("path", CODEOWNERS_PATH)
        messages.append(f"GitHub syntax error at {path}:{line} — {message}")
    return messages


def detect_template(normalized: str) -> str | None:
    standard = normalize_content(f"{CODEOWNERS_HEADER}\n{STANDARD_RULE}\n")
    restricted = normalize_content(f"{CODEOWNERS_HEADER}\n{RESTRICTED_RULE}\n")
    if normalized == standard:
        return "standard"
    if normalized == restricted:
        return "restricted"
    return None


def validate_branch(repo: str, branch: str) -> Finding:
    issues: list[str] = []
    template = ""

    if not branch_exists(repo, branch):
        return Finding(repo, branch, "skipped", "", ["branch not found"])

    content, path = fetch_codeowners_content(repo, branch)
    if content is None:
        return Finding(repo, branch, "invalid", "", ["CODEOWNERS file missing"])

    if path != CODEOWNERS_PATH:
        issues.append(f"CODEOWNERS found at {path}, expected {CODEOWNERS_PATH}")

    normalized = normalize_content(content)
    template = detect_template(normalized) or "non-standard"
    if template == "non-standard":
        issues.append("content does not match standard or restricted template")

    owners = extract_owners(content)
    if REQUIRED_OWNER not in owners:
        issues.append(f"missing required owner: @{REQUIRED_OWNER}")

    unexpected = sorted(owners - {"nilesh-sk", "naveenv-devops"})
    if unexpected:
        issues.append(f"unexpected owners: {', '.join('@' + o for o in unexpected)}")

    issues.extend(github_syntax_errors(repo, branch))

    if issues:
        return Finding(repo, branch, "invalid", template, issues)
    return Finding(repo, branch, "valid", template, [])


def write_report(findings: list[Finding], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["Repository,Branch,Status,Template,Issues"]
    for f in findings:
        issue_text = " | ".join(f.issues).replace('"', '""')
        lines.append(f'"{f.repo}","{f.branch}","{f.status}","{f.template}","{issue_text}"')
    try:
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except PermissionError:
        alt = out_path.with_name(out_path.stem + "-latest.csv")
        alt.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Note: wrote report to {alt} (original file locked)")


def print_invalid(findings: list[Finding]) -> None:
    invalid = [f for f in findings if f.invalid and f.status != "skipped"]
    if not invalid:
        print("All checked branches are valid.")
        return

    print(f"INVALID CODEOWNERS ({len(invalid)} branch entries):\n")
    print(f"{'Repository':<35} {'Branch':<18} {'Template':<12} Issues")
    print("-" * 110)
    for f in invalid:
        issue_text = "; ".join(f.issues)
        print(f"{f.repo:<35} {f.branch:<18} {f.template:<12} {issue_text}")


def main() -> int:
    repos = list_repos()
    findings: list[Finding] = []

    print(f"Org: {ORG}")
    print(f"Repositories: {len(repos)}")
    print(f"Branches: {', '.join(TARGET_BRANCHES)}")
    print("Mode: READ-ONLY validation")
    print()

    for repo in repos:
        for branch in TARGET_BRANCHES:
            findings.append(validate_branch(repo, branch))

    counts: dict[str, int] = {}
    for f in findings:
        counts[f.status] = counts.get(f.status, 0) + 1

    print("Summary:")
    for status in ("valid", "invalid", "skipped"):
        if status in counts:
            print(f"  {status}: {counts[status]}")
    print()

    print_invalid(findings)

    out_path = Path(__file__).resolve().parents[1] / "reports" / "codeowners-validation.csv"
    write_report(findings, out_path)
    print(f"\nReport: {out_path}")

    return 1 if counts.get("invalid", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
