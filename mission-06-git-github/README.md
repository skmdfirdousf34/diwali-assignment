# Mission 6 — Git and GitHub

## 1. Task / objective
The goal of Mission 6 was to understand version control principles and master the fundamental Git and GitHub collaboration workflow:
- Understand the core Git cycle: checking repository status, staging specific changes, creating meaningful commits, and viewing commit history.
- Distinguish between staging an edit and committing it.
- Create, use, and publish a separate development branch (`update-about`).
- Add a new "My Learning" section on that branch and push it to GitHub.
- Understand Pull Requests (PRs), how code review works, and merge branch changes back into `main`.
- Construct a comprehensive Git command glossary covering essential day-to-day operations.

---

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Shows which branch you are on, which files have been modified or untracked, and which files are currently staged in the index ready for commit. |
| **Stage selected changes (`git add <file>`)** | Moves specific modified files from the working directory into the staging area (index), preparing them to be part of the next commit snapshot. |
| **Create a commit (`git commit -m "..."`)** | Permanently records the staged changes as a new snapshot in the repository's history, accompanied by a descriptive commit message. |
| **View commit history (`git log`)** | Displays a chronological log of all previous commits, showing their unique SHA hashes, authors, timestamps, and commit messages. |

#### Difference between Staging and Committing:
- **Staging (`git add`):** Think of staging like packing a box. When you make changes across several files, you might only want to save some of them right now. Staging lets you choose exactly which files or lines belong in the next snapshot.
- **Committing (`git commit`):** Committing is sealing the box and putting a permanent label and timestamp on it. It permanently writes the staged snapshot into the repository's `.git` database. If you edit a file but don't stage it, it won't be saved in the commit.

---

### Task 6.2 — Create and use a branch
1. Created and switched to a new branch named `update-about`:
   ```bash
   git checkout -b update-about
   ```
2. Opened root `README.md` and added the section `## My Learning` summarizing 4 key takeaways from earlier missions.
3. Inspected the change with `git status` (showed `modified: README.md`).
4. Staged the file:
   ```bash
   git add README.md
   ```
5. Committed the change:
   ```bash
   git commit -m "Add My Learning section to root README on update-about branch"
   ```
6. Published the branch to GitHub:
   ```bash
   git push -u origin update-about
   ```

---

### Task 6.3 — Create a Pull Request
- **Pull Request concept & workflow:**
  - On GitHub, the `update-about` branch was compared against `main`.
  - The branch diff showed only the 9 added lines in `README.md`.
  - PR target: `update-about` $\to$ `main`.
  - **PR Status:** The branch was pushed to GitHub (`https://github.com/skmdfirdousf34/diwali-assignment/tree/update-about`). To complete the local workflow and keep the project up to date, the branch was merged into `main` using `git checkout main && git merge update-about` (fast-forward merge), and pushed to origin so `main` contains the updated learning notes. The remote `update-about` branch remains published on GitHub as evidence of branch creation and PR readiness.
- **Why branches and Pull Requests are useful:**
  - **Branches** allow team members to work on separate bugs or features simultaneously in isolated sandboxes without overwriting each other's code or breaking the stable production branch (`main`).
  - **Pull Requests (PRs)** provide a collaborative checkpoint where peers and senior developers can review code diffs, leave comments, suggest improvements, and run automated testing before changes are permanently merged into the main project.

---

### Task 6.4 — Git command glossary

| Operation | Command | One-line explanation in my own words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Starts Git version tracking inside the current folder, creating a hidden `.git` folder. |
| **Check status** | `git status` | Displays working tree status, showing staged, unstaged, and untracked files. |
| **Stage changes** | `git add <file>` | Adds modified or newly created files to the staging area for the next commit. |
| **Commit changes** | `git commit -m "<message>"` | Takes a permanent snapshot of currently staged files with an explanatory note. |
| **View history** | `git log --oneline` | Displays a condensed list of previous commits with their short hashes and messages. |
| **Create or list branches** | `git branch` | Lists all local branches, highlighting the currently active branch with an asterisk. |
| **Switch branches** | `git checkout <branch>` / `git switch <branch>` | Switches HEAD and working directory files to the specified branch. |
| **Publish changes** | `git push origin <branch>` | Uploads local commits from your computer up to the remote repository on GitHub. |
| **Retrieve remote changes** | `git pull origin <branch>` | Downloads commits from the remote repository and automatically merges them locally. |

---

## 3. Commands / tools used
- `git status`: Inspected repository working tree state.
- `git checkout -b update-about`: Created and switched to the feature branch.
- `git add README.md`: Staged the modified root README.
- `git commit -m "..."`: Recorded the commit snapshot.
- `git push -u origin update-about`: Published the feature branch to GitHub.
- `git checkout main`: Switched back to the main branch.
- `git merge update-about`: Merged the feature branch changes into main.
- `git push origin main`: Pushed the merged changes to the remote main branch.
- `git log --oneline --graph --all`: Inspected the complete multi-branch commit graph.

## 4. My understanding
- Git works locally on your machine even without internet, while GitHub is a cloud hosting service that makes sharing and collaborating with others possible.
- The three main stages in Git are: Working Directory $\to$ Staging Area (Index) $\to$ Committed Repository.
- Branches are lightweight pointers to commits. Merging incorporates changes from one branch pointer into another.

## 5. Difficulties faced
- In the beginning, it was easy to forget that creating a branch locally does not automatically create it on GitHub. Trying to run a plain `git push` on a new branch gives an upstream error.

## 6. How I resolved them
- Git's error message suggested using `git push --set-upstream origin update-about` (or `-u`), which establishes the remote tracking branch and pushes cleanly.

## 7. Evidence / files
- `mission-06-git-github/README.md` (this file)
- Branch `update-about` published to GitHub: [https://github.com/skmdfirdousf34/diwali-assignment/tree/update-about](https://github.com/skmdfirdousf34/diwali-assignment/tree/update-about)
- Updated root `README.md` with "My Learning" section.

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
