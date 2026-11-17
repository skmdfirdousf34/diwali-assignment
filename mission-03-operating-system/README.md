# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 was to explore the core roles and responsibilities of an Operating System:
- Inspect system hardware, kernel information, user accounts, and disk storage from the Terminal.
- Observe active processes, understand what a Process ID (PID) is, and see how the OS schedules tasks.
- Learn the difference between absolute and relative file paths, and decipher Unix file permission strings (`r`, `w`, `x`).
- Explain the key responsibilities of an Operating System in plain words with everyday examples.

---

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS name, kernel build, and processor architecture. | macOS 27.0.1 running Darwin Kernel Version 27.0.0 on Apple Silicon (`arm64`). |
| **Current account identity** | Identifies the currently active user account and shell. | Logged-in user is `[redacted]`, active login shell is `/bin/zsh`. |
| **Available and used storage** | Shows filesystem partitions, total storage capacity, used space, and free space. | Main volume `/dev/disk3s1s1`: Total `460Gi`, Used `13Gi`, Available `314Gi` (4% disk usage). |
| **System activity snapshot** | Shows a real-time overview of CPU load, memory usage, and number of running tasks. | CPU load idle at ~85-90%, unified memory actively shared across macOS daemons, editor, and background tasks. |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is simply a program in execution. When an application like VS Code or Python sits on disk, it is just static code; once you run it, the OS loads it into RAM, assigns it memory, and gives it CPU time — that running instance is a process.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to identify and track each running process. The OS uses PIDs to allocate resources, monitor performance, and terminate (kill) processes if they crash.
- **Two examples of processes running on my computer:**
  1. `WindowServer` (PID `446`): The essential macOS system graphics compositor process that manages windows, displays, and screen rendering.
  2. `duetexpertd` (PID `844`): A macOS background daemon process handling system resource activity and proactive system services.

---

### Task 3.3 — Understand paths and permissions

#### Absolute vs. Relative Paths
- **Absolute Path:** The complete, unambiguous path from the root directory (`/`) of the filesystem all the way to the target file or directory.
  - *Example from assignment folder:* `/Users/[redacted]/Documents/GitHub/diwali-assignment/README.md`
- **Relative Path:** The path evaluated relative to the current working directory where the terminal is currently positioned.
  - *Example from assignment folder:* `./mission-03-operating-system/README.md` (or simply `terminal-practice/practice.txt`)

#### File Permissions Observation
Running `ls -l terminal-practice/practice.txt` gave:
`-rw-r--r--@ 1 [redacted] staff 88 Nov 17 10:35 practice.txt`

| Permission | Meaning | Example | Status for Owner on `practice.txt` |
| :--- | :--- | :--- | :--- |
| **r — Read** | Allows opening and reading the file contents. | Opening a text file or viewing source code. | **Yes (`r`)** — Owner can read. |
| **w — Write** | Allows editing, modifying, or deleting the file. | Editing code or saving new changes. | **Yes (`w`)** — Owner can write. |
| **x — Execute** | Allows running the file as a program or script; on directories, allows entering/traversing. | Running a `.sh` shell script or Python binary. | **No (`-`)** — Not marked as executable. |

- **Permission breakdown:**
  - First character `-`: Regular file.
  - Characters 2-4 (`rw-`): **Owner** permissions (read and write, no execute).
  - Characters 5-7 (`r--`): **Group** permissions (read-only).
  - Characters 8-10 (`r--`): **Others** permissions (read-only).

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | The OS decides which program gets to use the CPU, how long it gets to run, and switches between processes so multiple apps can run smoothly together. | When you have a browser, music player, and code editor open, the OS switches between them so music plays without stuttering while you type. |
| **Memory management** | The OS keeps track of every byte of RAM, allocates memory blocks to apps that need them, and safely reclaims memory when programs close. | When you open a 50-tab browser window, the OS gives it 2GB of RAM, and when you quit the browser, that 2GB is freed for other programs. |
| **Device management** | The OS uses device drivers to communicate with hardware components like keyboards, displays, speakers, and external drives so software can talk to them easily. | When you plug in a USB flash drive, the OS detects the hardware, mounts the storage device, and lets you drag and drop files onto it. |
| **File management** | The OS organizes data on the SSD/HDD into structured directories and files, keeping track of where files physically reside on disk, their names, and sizes. | Saving a file called `notes.txt` inside `~/Documents/GitHub/` — the OS finds free blocks on the SSD and updates the folder catalog. |
| **User interface / shell** | Provides a way for users to interact with the computer, either visually with buttons and windows (GUI) or with typed commands (CLI). | The macOS graphical desktop (Finder) or the command-line shell (`zsh` in Terminal) where commands are typed. |
| **Security and permissions** | Protects the system by checking that users and apps only access data they are authorized to touch, preventing unauthorized access or accidental corruption. | File permission modes (`chmod`) preventing other non-admin users on the machine from reading or modifying your personal documents. |

---

## 3. Commands / tools used
- `uname -a`: Displayed OS kernel version and machine architecture (`arm64`).
- `sw_vers`: Showed macOS version (`macOS 27.0.1`).
- `whoami`: Checked the currently logged-in account name.
- `df -h /`: Displayed available and used disk space on the root drive in human-readable format.
- `ps aux | head -n 10`: Viewed running processes, PID numbers, and CPU/memory percentages.
- `ls -l`: Inspected file permissions and owners.

## 4. My understanding
- The OS acts as the brain and referee of the entire computer. Without the OS, applications would fight over the CPU and RAM and crash into each other.
- PIDs are crucial because every running program has one; if a program freezes, the OS can kill that specific PID without restarting the whole computer.
- File permissions (`r`, `w`, `x`) are divided into Owner, Group, and Everyone else, which is how Unix protects system files from being deleted accidentally by normal programs.

## 5. Difficulties faced
- Reading `ps aux` output at first was overwhelming because hundreds of background services show up with strange names and flags.

## 6. How I resolved them
- I piped `ps aux` to `head -n 10` so I could focus on understanding just the column headings (`USER`, `PID`, `%CPU`, `%MEM`, `COMMAND`) and identify familiar processes like WindowServer.

## 7. Evidence / files
- `mission-03-operating-system/README.md` (this file)

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
