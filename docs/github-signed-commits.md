# Signed Commits Setup

`dev` and `devops-testing` branches require **verified signed commits**. This guide is for all developers in **metapercept-metr**.

**Last updated:** June 2026

---

## Why signed commits?

The **Secure Branch Protection Ruleset** enforces `required_signatures` on `dev` and `devops-testing`. Unsigned commits block PR merges with:

> *Commits must have verified signatures.*

Each developer must sign their **own** commits. A CODEOWNER's SSH key on their laptop does not sign another person's work.

---

## Option A — SSH commit signing (recommended)

Works well on Windows, macOS, and Linux. Uses your existing SSH key or a dedicated signing key.

### 1. Generate a signing key (or use existing)

```bash
ssh-keygen -t ed25519 -C "your-email@company.com" -f ~/.ssh/id_ed25519_signing
```

### 2. Add public key to GitHub

1. Copy the public key:
   ```bash
   cat ~/.ssh/id_ed25519_signing.pub
   ```
2. GitHub → **Settings → SSH and GPG keys → New SSH key**
3. Key type: **Signing Key**
4. Paste public key and save

### 3. Configure Git

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519_signing.pub
git config --global commit.gpgsign true
```

On Windows (Git Bash), the path may be:
```bash
git config --global user.signingkey "C:/Users/YourName/.ssh/id_ed25519_signing.pub"
```

### 4. Verify

```bash
git commit --allow-empty -S -m "test signed commit"
git log --show-signature -1
```

Push to a test branch and confirm the **Verified** badge appears on GitHub.

---

## Option B — GPG commit signing

### 1. Generate GPG key

```bash
gpg --full-generate-key
# Select: RSA and RSA, 4096 bits, your email
```

### 2. List key ID

```bash
gpg --list-secret-keys --keyid-format=long
# Copy the key ID after "rsa4096/"
```

### 3. Add to GitHub

```bash
gpg --armor --export YOUR_KEY_ID
```

GitHub → **Settings → SSH and GPG keys → New GPG key** → paste armored key.

### 4. Configure Git

```bash
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true
```

---

## Fixing unsigned commits on an existing PR branch

If your PR was opened before signing was set up, rewrite the branch with signed commits.

### Squash into one signed commit (simplest)

```bash
git checkout your-feature-branch
git fetch origin
git rebase origin/dev

git reset --soft origin/dev
git commit -S -m "MDP-XXX: description of all changes"
git push --force-with-lease
```

### Re-sign multiple commits (interactive rebase)

```bash
git rebase origin/dev
# Mark each commit for reword/edit and amend with -S:
git commit --amend -S --no-edit
git rebase --continue
git push --force-with-lease
```

> After force-push, **all PR approvals are dismissed**. Reviewers must re-approve.

---

## Verify on GitHub

| Indicator | Meaning |
|---|---|
| **Verified** badge on commit | Signing configured correctly |
| No badge | Commit is unsigned — merge will be blocked on `dev` |
| **Unverified** badge | Key not added to GitHub account |

---

## Platform notes

### Windows (Git Bash / MINGW64)

```bash
# Ensure ssh-agent is running
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_signing

git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519_signing.pub
git config --global commit.gpgsign true
```

### VS Code

Enable in settings:
```json
"git.enableCommitSigning": true
```

### GitHub CLI commits

```bash
gh auth login
# Commits via gh pr merge use GitHub's signing when merged via web UI
```

---

## FAQ

| Question | Answer |
|---|---|
| Does my CODEOWNER need to sign my commits? | **No.** You sign your own commits. |
| Does squash merge create a signed commit? | The merge commit is signed by GitHub if merged via web UI, but branch commits must still be signed for PR checks. |
| I already have an SSH key for authentication | Create a separate **signing key** or use the same key as a Signing Key in GitHub settings. |
| Can admin bypass the signing rule? | Org admins can bypass rulesets — emergency use only. |

---

## Related documents

- [PR Merge Guide](github-pr-merge-guide.md)
- [Branch Protection Rules](github-branch-protection.md)
- [GitHub docs — Signing commits](https://docs.github.com/en/authentication/managing-commit-signature-verification)
