# Mission 8 — Final review and submission

## 1. Task / objective
The objective of Mission 8 was to conduct a comprehensive final review of the entire "Digital Detective" repository before submission:
- Verify that all mission folders (Missions 00 through 08) and files are present, complete, and properly structured.
- Ensure every mission has its dedicated `README.md` formatted with the required standardized sections.
- Verify that every mission has at least one dedicated, meaningful commit pushed to the public GitHub repository.
- Verify that the root `README.md` is complete with student details, index, topic review, and instructions for running the converter.
- Ensure all personal information (usernames, local IPs, network credentials) has been sanitized and redacted.
- Complete the final 14-point submission checklist.

---

## 2. Work completed

### Repository Review & Verification
- Checked directory hierarchy: all 9 mission folders and the `evidence/` folder are correctly populated.
- Checked scripts:
  - `mission-04-programs/hello.py` executed cleanly.
  - `mission-05-numbers-data/number_converter.py` tested successfully with multiple inputs (42, 255, 1024).
- Checked Git branch and commit history:
  - Branch `update-about` was created, committed to, pushed to GitHub, and merged into `main`.
  - Every mission has an individual, descriptive commit pushed to GitHub.
- Redaction audit:
  - Local macOS username replaced with `[redacted]`.
  - Local gateway and DNS resolver IP addresses replaced with `[redacted-dns-server]`.
  - No personal Wi-Fi SSIDs, access tokens, or private paths are exposed.

---

### Mission Completion Status

| Mission | Folder | Status | Key Output / Deliverable |
| :--- | :--- | :--- | :--- |
| **Mission 0** | `mission-00-setup/` | Completed | Repo initialized, versions verified, directory skeleton created. |
| **Mission 1** | `mission-01-computer-basics/` | Completed | IPOS cycle trace, hardware/software tables, embedded systems analysis. |
| **Mission 2** | `mission-02-terminal/` | Completed | Command reference table, safe file editing, flags/pipes, Homebrew notes. |
| **Mission 3** | `mission-03-operating-system/` | Completed | OS specs, PID process analysis, path/permissions breakdown, OS roles. |
| **Mission 4** | `mission-04-programs/` | Completed | `hello.py` executed, compiler vs. interpreter comparison table. |
| **Mission 5** | `mission-05-numbers-data/` | Completed | Manual base conversion workings, Python checks, `number_converter.py`, ASCII/UTF-8 notes. |
| **Mission 6** | `mission-06-git-github/` | Completed | Branching (`update-about`), commit lifecycle, PR workflow, Git glossary. |
| **Mission 7** | `mission-07-networking/` | Completed | Networking concepts table, `ping` & `nslookup` tests, 6-step website load flow. |
| **Mission 8** | `mission-08-final-report/` | Completed | Final review, submission checklist, root README update, final commit. |

---

### Step 4 — Final Submission Checklist

- [x] **All mission folders are present and each has its own README.md.** (Missions 00 through 08 all contain complete `README.md` files).
- [x] **Every mission README records the task, commands/tools used, understanding and difficulties.** (Consistent 8-heading template followed across all missions).
- [x] **Every mission has its own meaningful commit, and all required commits are pushed.** (Verified in Git log, zero lumped commits).
- [x] **IPOS, hardware, software and computer-system examples are included.** (Mission 1 covers all 3 tables with detailed examples).
- [x] **Terminal operations, file management, flags and pipes are explained.** (Mission 2 covers `pwd`, `ls -lah`, `cp`, `mv`, `cat`, and `| head -n 5`).
- [x] **Operating system, processes, paths, storage and permissions are covered.** (Mission 3 covers macOS specs, PIDs, absolute/relative paths, and `rw-r--r--`).
- [x] **Compiler and interpreter are compared.** (Mission 4 includes detailed comparison table and paragraph).
- [x] **Number conversions include working and Python verification.** (Mission 5 shows manual division/expansion steps and Python shell verification).
- [x] **The number_converter.py program runs successfully with at least three test values.** (Tested with 42, 255, and 1024).
- [x] **Git commit history, branch and Pull Request activity are visible.** (Branch `update-about` pushed to remote; merge history preserved).
- [x] **LAN, MAN, WAN, DNS, router, protocols and client-server are explained.** (Mission 7 includes full table and 6-step website load flow).
- [x] **The root README explains the project and how to run the converter.** (Root README includes student details, index, learning, and execution instructions).
- [x] **Personal information has been removed from screenshots and outputs.** (All usernames, paths, and local network IPs are redacted).
- [x] **All final changes are committed and pushed to GitHub.** (Final commit pushed to GitHub remote).

---

## 3. Commands / tools used
- `git status`: Checked for clean working tree before final wrap-up.
- `git log --oneline --graph --all`: Verified all commits and branch points.
- `ls -R`: Confirmed presence of all mission files and scripts.
- Text Editor (VS Code): Final polish on documentation formatting and checklist.

## 4. My understanding
- System thinking is the biggest takeaway from this assignment. Before starting, concepts like terminal commands, Git commits, binary numbers, and web requests felt like separate, isolated topics.
- Connecting them together showed me that everything in a computer is a layered abstraction: hardware switches execute binary; compilers/interpreters turn human code into machine instructions; the OS manages memory and processes; Git tracks file changes over time; and networking protocols allow these processes to exchange packets across the globe.

## 5. Difficulties faced
- Keeping every mission strictly isolated and ensuring each had its own meaningful commit without accidentally staging files from other missions took discipline.
- Making sure sensitive information like personal home paths and Wi-Fi IP addresses were not committed required careful review before running `git add`.

## 6. How I resolved them
- I always ran `git status` and `git diff` before committing to inspect exactly what was staged, and used `[redacted]` placeholders wherever system outputs contained sensitive local identifiers.

## 7. Evidence / files
- `mission-08-final-report/README.md` (this file)
- Complete repository tree on GitHub: [https://github.com/skmdfirdousf34/diwali-assignment](https://github.com/skmdfirdousf34/diwali-assignment)

## 8. Commit details
- **Commit message:** `Complete final report and verify assignment submission`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
