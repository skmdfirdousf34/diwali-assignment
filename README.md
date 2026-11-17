# The Digital Detective — Diwali Independent Learning Assignment
**Explore Your Computer • Build a Mini System Report**

## Student Details
| Field | Details |
| :--- | :--- |
| **Name** | Sk Md Firdous |
| **USN** | 2392608513 |
| **Campus / Section** | NST Bangalore / Section B1 |
| **GitHub Username** | [skmdfirdousf34](https://github.com/skmdfirdousf34) |
| **Repository Name** | diwali-assignment |
| **Repository URL** | [https://github.com/skmdfirdousf34/diwali-assignment](https://github.com/skmdfirdousf34/diwali-assignment) |

---

## Assignment Overview
This repository documents my independent hands-on investigation for "The Digital Detective" assignment. As a first-year Computer Science Engineering student, the goal was to explore how my computer actually works beneath the graphical interface — investigating terminal operations, file systems and permissions, operating system process scheduling, compiler vs. interpreter execution models, number systems (decimal, binary, hexadecimal) and text encodings, Git/GitHub collaboration workflows, and basic computer networking.

Every single mission was carried out sequentially on my macOS system, documented inside its own dedicated folder with its own `README.md`, and recorded with a distinct, descriptive Git commit.

---

## Mission Index
| Mission | Focus Area | Mission Folder / Link | Status |
| :--- | :--- | :--- | :--- |
| **Mission 0** | Repository and workspace setup | [mission-00-setup](./mission-00-setup/README.md) | Completed |
| **Mission 1** | Computer fundamentals and IPOS | [mission-01-computer-basics](./mission-01-computer-basics/README.md) | Completed |
| **Mission 2** | Terminal and file management | [mission-02-terminal](./mission-02-terminal/README.md) | Completed |
| **Mission 3** | Operating system, processes and permissions | [mission-03-operating-system](./mission-03-operating-system/README.md) | Completed |
| **Mission 4** | How programs run | [mission-04-programs](./mission-04-programs/README.md) | Completed |
| **Mission 5** | Number systems, Python and text encoding | [mission-05-numbers-data](./mission-05-numbers-data/README.md) | Completed |
| **Mission 6** | Git, GitHub, branches and Pull Requests | [mission-06-git-github](./mission-06-git-github/README.md) | Completed |
| **Mission 7** | Computer networks | [mission-07-networking](./mission-07-networking/README.md) | Completed |
| **Mission 8** | Final review and submission checklist | [mission-08-final-report](./mission-08-final-report/README.md) | Completed |

---

## Topics Explored
1. **Computer Hardware & IPOS Cycle**: Tracing input, processing, output, and persistent storage using a code-editing workflow; classifying hardware, OS, application, and utility software; and analyzing embedded systems (ATMs, ticket machines, traffic lights).
2. **Terminal Operations & File Management**: Navigating directories, manipulating files with safe append/backup habits, utilizing flags (`-l`, `-a`, `-h`), piping outputs (`|`), and inspecting package managers (Homebrew).
3. **Operating System Architecture**: macOS kernel inspection (`arm64`), storage analysis, tracking running processes by PID, distinguishing absolute vs. relative paths, and reading Unix file permissions (`rwx`).
4. **Program Execution Models**: Comparing compiled languages (C/C++) versus interpreted languages (Python) and executing `hello.py`.
5. **Data Representation & Encodings**: Manual and Python-verified conversions between Decimal, Binary, and Hexadecimal; ASCII and UTF-8 text encodings; and an interactive converter script (`number_converter.py`).
6. **Git Version Control & Collaboration**: Working directory vs. staging vs. commit history, branch creation (`update-about`), Pull Request review workflows, and a Git glossary.
7. **Computer Networks**: Network classifications (LAN, MAN, WAN), DNS resolution, routing, packet switching, client-server models, and network diagnostic tools (`ping`, `nslookup`).

---

## My Learning
Completing this assignment gave me a much stronger foundation in how computers actually operate:
1. **The Terminal is Powerful:** Moving away from GUI clicking to terminal commands (`cd`, `ls -lah`, `cp`, `mv`, and pipes) makes inspecting and manipulating files much faster and scriptable.
2. **The Operating System Coordinates Everything:** Understanding that every app is a process with its own PID, allocated memory, and permissions made me appreciate how macOS prevents apps from crashing each other.
3. **Data Representation Connects Math to Hardware:** Seeing how transistors (binary) translate into 4-bit hexadecimal nibbles and character encoding standards (ASCII/Unicode) clarified how simple electrical states produce text, numbers, and multimedia.
4. **Git is Essential for Software Engineering:** Learning to stage selectively, commit with clear messages, branch for experiments, and merge cleanly showed me how real engineering teams collaborate safely.

---

## How to Run the Number Converter
To run the interactive Python number converter written for Mission 5:

1. Open your Terminal.
2. Navigate to the `mission-05-numbers-data` directory:
   ```bash
   cd mission-05-numbers-data
   ```
3. Run the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
4. Enter any positive decimal integer (e.g. `42`, `255`, or `1024`) to view its binary and hexadecimal representations.

---

## Separate Mission Commits
In accordance with the assignment guidelines, each mission was completed and committed separately. No batch commits were made. You can review the chronological development log using:
```bash
git log --oneline --graph --all
```

---

## Privacy Note
In compliance with assignment instructions, personal and sensitive information such as local user account paths, hardware serial numbers, Wi-Fi network names, and private local IP addresses have been masked or replaced with `[redacted]` throughout this repository.
