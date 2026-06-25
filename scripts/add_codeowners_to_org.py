#!/usr/bin/env python3
"""Add .github/CODEOWNERS to dev, devops-testing, and main branches across org repos."""

from __future__ import annotations

import base64
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ORG = "metapercept-metr"
TARGET_BRANCHES = ("dev", "devops-testing", "main")
CODEOWNERS_PATH = ".github/CODEOWNERS"
COMMIT_MESSAGE = "chore: add standard CODEOWNERS for dev, devops-testing, and main"
CODEOWNERS_CONTENT = """# This is a basic CODEOWNERS file.
# See https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners for details on how to specify code owners.

*  @nilesh-sk @naveenv-devops
"""


@dataclass
class Result:
    repo: str
    branch: str
    status: str
    detail: str = ""


@dataclass
class RunReport:
    results: list[Result] = field(default_factory=list)

    def add(self, repo: str, branch: str, status: str, detail: str = "") -> None:
        self.results.append(Result(repo, branch, status, detail))

    def summary(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for r in self.results:
            counts[r.status] = counts.get(r.status, 0) + 1
        return counts


def gh_api(
    method: str,
    endpoint: str,
    *,
    fields: dict[str, str] | None = None,
) -> object | None:
    cmd = ["gh", "api", "-X", method, endpoint]
    for key, value in (fields or {}).items():
        cmd.extend(["-f", f"{key}={value}"])
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        stderr = proc.stderr or ""
        if "404" in stderr:
            return None
        raise subprocess.CalledProcessError(
            proc.returncode, cmd, output=proc.stdout, stderr=proc.stderr
        )
    if not proc.stdout.strip():
        return None
    return json.loads(proc.stdout)


def gh_json(endpoint: str) -> object:
    result = gh_api("GET", endpoint)
    if result is None:
        raise subprocess.CalledProcessError(1, ["gh", "api", endpoint])
    return result


def list_repos() -> list[str]:
    proc = subprocess.run(
        [
            "gh",
            "api",
            f"orgs/{ORG}/repos?per_page=100",
            "--paginate",
        ],
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


def get_existing_sha(repo: str, branch: str) -> str | None:
    for path in (CODEOWNERS_PATH, "CODEOWNERS"):
        data = gh_api(
            "GET",
            f"repos/{ORG}/{repo}/contents/{path}?ref={branch}",
        )
        if data and isinstance(data, dict) and data.get("sha"):
            return data["sha"]
    return None


def put_codeowners(repo: str, branch: str, sha: str | None) -> None:
    payload = {
        "message": COMMIT_MESSAGE,
        "content": base64.b64encode(CODEOWNERS_CONTENT.encode("utf-8")).decode("ascii"),
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha

    gh_api("PUT", f"repos/{ORG}/{repo}/contents/{CODEOWNERS_PATH}", fields=payload)


def process_repo(repo: str, report: RunReport, dry_run: bool) -> None:
    for branch in TARGET_BRANCHES:
        if not branch_exists(repo, branch):
            report.add(repo, branch, "skipped", "branch not found")
            continue

        existing_sha = get_existing_sha(repo, branch)
        if existing_sha:
            report.add(repo, branch, "already_exists", "CODEOWNERS present; updating")
        else:
            report.add(repo, branch, "pending", "will create")

        if dry_run:
            continue

        try:
            put_codeowners(repo, branch, existing_sha)
            report.results[-1].status = "updated" if existing_sha else "created"
            report.results[-1].detail = ""
        except subprocess.CalledProcessError as exc:
            detail = (exc.stderr or exc.stdout or str(exc)).strip().replace("\n", " ")
            report.results[-1].status = "failed"
            report.results[-1].detail = detail[:300]


def write_report(report: RunReport, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = ["Repository,Branch,Status,Detail"]
    for r in report.results:
        detail = r.detail.replace('"', '""')
        lines.append(f'"{r.repo}","{r.branch}","{r.status}","{detail}"')
    (out_dir / "codeowners-rollout.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    repos = list_repos()
    report = RunReport()

    print(f"Org: {ORG}")
    print(f"Repositories: {len(repos)}")
    print(f"Branches: {', '.join(TARGET_BRANCHES)}")
    print(f"Mode: {'DRY RUN' if dry_run else 'APPLY'}")
    print()

    for repo in repos:
        process_repo(repo, report, dry_run)

    out_dir = Path(__file__).resolve().parents[1] / "reports"
    write_report(report, out_dir)

    counts = report.summary()
    print("Summary:")
    for status, count in sorted(counts.items()):
        print(f"  {status}: {count}")
    print(f"\nReport: {out_dir / 'codeowners-rollout.csv'}")

    failed = counts.get("failed", 0)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
