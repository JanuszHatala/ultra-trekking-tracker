# Git & Contribution Governance Rules

This repository belongs strictly and exclusively to **Janusz Hatala** (`JanuszHatala`).
All development and automated assistant actions in this repository must strictly adhere to the following governance rules:

## 1. Zero Direct Commits to `main`
- All changes, features, bug fixes, and chores **MUST** be performed on dedicated semantic branches:
  - `feat/<short-description>` for new features or capabilities
  - `fix/<short-description>` for bug fixes and patches
  - `chore/<short-description>` for maintenance, dependencies, configuration, or docs
- Direct pushes or commits to `main` are strictly forbidden.

## 2. Mandatory Identity Enforcement
- Commits **MUST** strictly and exclusively use the personal identity:
  - **Name**: `Janusz Hatala`
  - **Email**: `janusz.hatala@gmail.com`
- **Zero Company Account Leakage**: Under NO circumstances may the company account (`januszhatala-tb`) or company email (`janusz.hatala@timebook.net`) appear in commit author/committer headers, git config, or PR metadata.
- Repository configuration must enforce:
  ```bash
  git config user.name "Janusz Hatala"
  git config user.email "janusz.hatala@gmail.com"
  ```

## 3. Local Verification Prior to Push
- All changes must be verified locally before pushing to remote:
  - Web checks: lint and build verification (`npm run lint`, `npm run build` where applicable).
  - Android checks: unit tests and build compilation (`./gradlew test --no-daemon`, `./gradlew assembleDebug --no-daemon`).
- Never push broken or unverified code to remote branches.

## 4. Pull Request Protocol
- All work branches must be pushed to remote origin.
- Open a Pull Request targeting `main` via `gh pr create`:
  ```bash
  gh pr create --base main --head <branch-name> --title "<type>: <description>" --body "<details>"
  ```
- All automated GitHub Actions CI status checks (`web-check`, `android-check`) must pass.
- Merge the Pull Request cleanly into `main` using `gh pr merge --squash` or `gh pr merge --merge`.
- Clean up the local and remote feature branch after merge, then update local `main`.
