# DevOps Prerequisites

Tools, access, and environment setup required for Met-R platform engineering.

---

## Access prerequisites

| Access | Required for | Request from |
|---|---|---|
| GitHub org `metapercept-metr` | All engineers | `@naveenv-devops` |
| Repository write access | Service development | DevOps lead |
| GitHub org admin (select) | Rulesets, bypass | DevOps lead only |
| Cloud portal (Azure/AWS) | Infrastructure | DevOps lead |
| Kubernetes cluster | Deployment | DevOps lead |
| Met-R staging workspace | Integration testing | Platform lead |

---

## Workstation software

### Required

| Tool | Minimum version | Purpose |
|---|---|---|
| **Git** | 2.40+ | Version control |
| **GitHub CLI (`gh`)** | 2.40+ | Org automation, API |
| **Python** | 3.11+ | Converter services, scripts |
| **Node.js** | 20 LTS | Frontend (`metR-Frontend`) |
| **Docker Desktop** | 4.x | Local service development |
| **PowerShell / Bash** | — | Scripting |

### Recommended

| Tool | Purpose |
|---|---|
| **kubectl** | Kubernetes management |
| **Terraform / Bicep** | Infrastructure as Code |
| **VS Code** | Primary IDE |
| **Postman / Insomnia** | API testing |

---

## Git configuration (mandatory)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@metapercept.com"
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519_signing.pub
git config --global commit.gpgsign true
```

Signed commits are **required** for `dev` and `devops-testing`. See [Signed commits](../github-signed-commits.md).

---

## SSH keys

| Key type | Purpose | GitHub setting |
|---|---|---|
| Authentication key | `git push` / `gh` | SSH key |
| Signing key | Verified commits | Signing key |

Generate signing key:
```bash
ssh-keygen -t ed25519 -C "your-email@metapercept.com" -f ~/.ssh/id_ed25519_signing
```

---

## Python environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt
pip install -r requirements-dev.txt   # if present
pytest                                 # verify tests run
```

---

## Docker local development

```bash
docker --version          # 24+
docker compose version    # v2
docker compose up -d      # per-service docker-compose.yml
```

---

## GitHub CLI authentication

```bash
gh auth login
# Select: GitHub.com → HTTPS or SSH → Login with browser

gh auth status
# Required scopes for DevOps scripts: repo, read:org, workflow
```

---

## Repository clone

```bash
gh repo clone metapercept-metr/metR-Converter-FrameMaker
cd metR-Converter-FrameMaker
git checkout dev
git pull origin dev
```

---

## CI local prerequisites

Before opening a PR, verify locally:

| Check | Command |
|---|---|
| Unit tests | `pytest` |
| Linting | `ruff check .` or project linter |
| XSLT validation | Project-specific script |
| Signed commit | `git log --show-signature -1` |

CI runs these as required checks on `main` / `feature/**`:
- `unit-tests-pytest`
- `xslt-validation`
- `dita-ot-schema-check`
- `security-scan`

---

## Pre-flight checklist (engineers)

```
☐ GitHub org access granted
☐ Git identity configured
☐ SSH signing key added to GitHub
☐ gh CLI authenticated
☐ Python 3.11+ and Node 20 installed
☐ Docker running
☐ Repository cloned; on correct branch
☐ Tests pass locally
☐ Read PR merge guide and branch protection rules
```

---

## Related

- [Engineer onboarding](onboarding.md)
- [DevOps licensing](licensing.md)
- [Platform prerequisites](../platform/prerequisites.md)
