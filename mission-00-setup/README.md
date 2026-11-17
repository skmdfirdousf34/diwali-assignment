# Mission 0 — Repository and workspace setup

## 1. Task / objective
The goal of Mission 0 was to set up my workspace for the entire "Digital Detective" assignment. I needed to verify that my development environment has Python 3 and Git installed, decide on the repository structure, create all required mission folders and markdown files, prepare the root README, and connect the local project to GitHub so that every subsequent mission can be tracked and pushed properly.

## 2. Work completed
- Decided on the repository name (`diwali-assignment`) matching my public GitHub repo.
- Created the main project folder locally under `~/Documents/GitHub/diwali-assignment`.
- Checked and noted the installed versions of Python 3 and Git from the Terminal.
- Created the complete folder structure with folders for Mission 00 through Mission 08 plus an `evidence/` folder.
- Created the root `README.md` containing my student information table, assignment overview, mission index, and topic list.
- Created this `mission-00-setup/README.md` following the required heading format.
- Initialized local Git tracking on branch `main` and set up the remote link to GitHub.

## 3. Commands / tools used
- `python3 --version`: Used to verify Python 3 is installed. Output showed `Python 3.14.7`.
- `git --version`: Used to verify Git is installed. Output showed `git version 2.54.0 (Apple Git-157)`.
- `mkdir -p`: Used to create the 9 mission folders and the evidence folder in one command.
- `touch`: Used to generate the empty markdown placeholder files for all missions.
- `git init -b main`: Initialized a new Git repository with `main` as the default branch.
- `git remote add origin https://github.com/skmdfirdousf34/diwali-assignment.git`: Connected the local folder to my GitHub remote repository.

## 4. My understanding
- **What is a Git repository?** A repository (or "repo") is like a smart folder that tracks every change made to the files inside it. Instead of saving copies like `project_final_v2.txt`, Git saves snapshots called commits. This means if I make a mistake or break some code later, I can always look back at earlier versions or restore them.
- **Why organize the folder structure by mission?** Having separate folders (`mission-00-setup`, `mission-01-computer-basics`, etc.) keeps all notes, tables, programs, and screenshots neatly organized according to topic. If everything was dumped into one single folder, it would become very messy and difficult for the instructor to review.

## 5. Difficulties faced
- Initially, I had to ensure that creating the local repo didn't cause a conflict with GitHub since GitHub sometimes asks you to add a README when creating a repo online. If both have different initial READMEs, `git push` gives an error about unrelated histories.

## 6. How I resolved them
- I created an empty repo on GitHub without checking the "Add a README file" box. Then I initialized locally, added the files, and set the remote URL so the first push goes smoothly.

## 7. Evidence / files
- Root `README.md`
- `mission-00-setup/README.md` (this file)
- Folder structure created:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Branch:** `main`
- **Pushed to GitHub:** Yes (verified on remote)
