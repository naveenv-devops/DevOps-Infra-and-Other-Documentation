# Engineer Onboarding

Checklist for new engineers joining the Met-R platform team.

---

## Prerequisites

Complete before Day 1: [DevOps prerequisites](prerequisites.md) · [Licensing](licensing.md)

---

## Day 1 — Access

- [ ] GitHub org invite: `metapercept-metr`
- [ ] Access to relevant repositories (based on team)
- [ ] Met-R workspace credentials (if applicable)
- [ ] Communication channels (Teams / Slack)

---

## Day 1 — Development setup

### Git & GitHub

```bash
# Git identity
git config --global user.name "Your Name"
git config --global user.email "your-email@metapercept.com"

# Commit signing (REQUIRED for dev branch)
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519_signing.pub
git config --global commit.gpgsign true
```

Add SSH signing key to GitHub → Settings → SSH keys → **Signing Key**.

Full guide: [Signed commits](../github-signed-commits.md)

### GitHub CLI

```bash
gh auth login
gh auth status
```

---

## Day 2 — Understand the platform

| Read | Time |
|---|---|
| [Platform architecture](../platform/architecture.md) | 30 min |
| [Services catalog](../platform/services-catalog.md) | 20 min |
| [CI/CD overview](ci-cd-overview.md) | 15 min |
| [PR merge guide](../github-pr-merge-guide.md) | 15 min |
| [Key concepts (product)](https://github.com/naveenv-devops/DevOps-Infra-and-Other-Documentation/blob/main/product-docs/docs/get-started/key-concepts.md) | 15 min |

---

## Day 3 — First contribution

1. Clone assigned service repository
2. Create feature branch: `feature/MDP-XXX-description`
3. Make a small change with **signed commit**
4. Open PR to `dev`
5. Request review from CODEOWNER (`@naveenv-devops` or `@nilesh-sk`)

---

## Branch rules reminder

| Branch | Signed commits | Reviews | CI |
|---|---|---|---|
| `dev` | **Yes** | 2 + CODEOWNER | Optional |
| `main` | No | 2 + CODEOWNER | **4 checks** |

---

## Who to contact

| Topic | Contact |
|---|---|
| GitHub access | `@naveenv-devops` |
| Technical questions | `@nilesh-sk` |
| Platform architecture | Platform lead |

---

## Related

- [DevOps README](README.md)
- [Runbooks](runbooks/README.md)
