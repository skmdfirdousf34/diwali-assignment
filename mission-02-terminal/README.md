# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 was to become confident using the command-line interface (CLI) in Terminal:
- Practise essential navigation and file management commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Safely create and modify files inside a designated practice folder (`terminal-practice`).
- Understand how command flags modify behavior and how pipes (`|`) chain commands together.
- Explore package managers (Homebrew on macOS) and understand why they are used in software development.

---

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full working directory path from the root folder. | Showed `/Users/[redacted]/Documents/GitHub/diwali-assignment`. |
| **Directory listing (`ls`)** | Lists names of files and subfolders in the current folder. | Displayed folder names like `mission-00-setup`, `mission-01-computer-basics`, `evidence`, etc. |
| **Detailed listing (`ls -l`)** | Displays a long-format listing with permissions, owner, size, and modification date. | Showed columns like `drwxr-xr-x`, user `[redacted]`, group `staff`, byte sizes, and timestamps. |
| **Change directory (`cd ..`)** | Moves the terminal prompt up one level into the parent directory. | Prompt changed from `diwali-assignment` to `GitHub`, and running `pwd` showed one folder up. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new folder inside the current directory. | A new folder named `terminal-practice` appeared in the listing. |
| **Create empty file (`touch practice.txt`)** | Creates an empty file or updates the timestamp of an existing file. | Created `practice.txt` with size 0 bytes. |
| **Copy file (`cp practice.txt practice_backup.txt`)** | Duplicates a file to a new destination or name. | Created an exact duplicate file named `practice_backup.txt`. |
| **Move / rename file (`mv practice_backup.txt practice_renamed_backup.txt`)** | Renames a file or moves it to a different directory. | The file `practice_backup.txt` was renamed to `practice_renamed_backup.txt`. |
| **Display file contents (`cat practice.txt`)** | Reads file contents and prints them directly to terminal stdout. | Printed the text lines stored inside the file onto my screen. |

---

### Task 2.2 — Practise file changes safely
Inside the `terminal-practice` folder:
1. Created `practice.txt` with line 1: `This is the first line of my practice file.` using `>`.
2. Appended line 2: `This is the second line added using append.` using `>>`.
3. Checked using `cat practice.txt`: Both lines were preserved properly.
4. Created a backup with `cp practice.txt practice_backup.txt`, then renamed it using `mv practice_backup.txt practice_renamed_backup.txt`.

**Questions answered:**
- **What is the difference between replacing a file's contents and adding text to the end?**
  Using the single redirect operator `>` overwrites the file entirely from scratch, replacing whatever was there before. Using the double redirect operator `>>` appends new text to the end of the existing file without deleting earlier lines.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) duplicates the file so two independent copies exist on disk. Moving (`mv`) changes the file's path or name, meaning only one instance remains and the original location is gone.
- **What information does the current-directory display provide?**
  The `pwd` (print working directory) command gives the complete, absolute path starting from the root filesystem (`/`) down to the folder you are currently sitting in. It keeps you from getting lost in nested subdirectories.
- **Why is a directory-listing operation useful?**
  Since the Terminal has no graphical icons, `ls` lets you see what files and folders are present, how they are spelled, whether they are hidden, and their sizes before you try reading or running them.

---

### Task 2.3 — Understand flags and pipes
- **Comparing listings:**
  - Running `ls`: Printed just the names of the folders in simple columns.
  - Running `ls -lah`: Printed detailed lines including hidden files (`-a` for dot-files like `.git`), permissions, link counts, owners, and sizes formatted in human-readable units like `88B` or `4.0K` (`-h`).
- **Understanding pipes (`|`):**
  - Command tested: `ls -lah | head -n 5`
  - **What the pipe does:** The pipe symbol `|` connects the standard output (stdout) of the command on the left directly into the standard input (stdin) of the command on the right without creating a temporary file on disk.
  - **Contribution of each side:**
    - Left side (`ls -lah`): Reads the directory and produces a long, detailed list of all files.
    - Right side (`head -n 5`): Receives that stream of text and trims it to display only the top 5 lines.

---

### Task 2.4 — Understand package managers
- **Check Homebrew status on macOS:**
  - Checked version: `brew --version` returned `Homebrew 7.0.9`.
  - Checked packages: `brew list` showed installed packages including `python@3.14`, `node`, `uv`, `ffmpeg`, etc.
- **Why package managers are useful:**
  A package manager is like an app store for command-line tools. Instead of manually downloading zip files from random websites, figuring out build instructions, and manually editing the system `PATH`, a package manager downloads, installs, configures, and automatically resolves all background dependencies with a single command (like `brew install python`). It also makes updating or removing software safe and clean.

---

## 3. Commands / tools used
- `pwd`: Checked current directory path.
- `ls`, `ls -l`, `ls -lah`: Listed directory contents with various flags.
- `cd`, `cd ..`: Navigated between folders.
- `mkdir`: Created folders (`terminal-practice`).
- `touch`: Created empty files.
- `echo "..." >` and `echo "..." >>`: Created and appended text to files safely.
- `cat`: Displayed file text.
- `cp` and `mv`: Copied and renamed files.
- `head -n 5`: Filtered top 5 lines of piped output.
- `brew --version`, `brew list`: Inspected macOS Homebrew package manager.

## 4. My understanding
- The terminal is much faster and more precise than clicking around in Finder once you know the commands.
- Flags modify commands: `-l` gives details, `-a` reveals hidden files, and `-h` converts raw bytes to readable KB/MB.
- Pipes allow chaining small, focused tools together (like listing files and filtering with `head`) to build powerful commands.

## 5. Difficulties faced
- In the beginning, I accidentally typed `ls - lah` with a space between `-` and `lah`, which gave an error because the terminal thought `lah` was a folder name rather than flags.

## 6. How I resolved them
- I learned that flags must be attached directly to the hyphen (e.g., `-lah` or `-l -a -h`), which fixed the syntax error immediately.

## 7. Evidence / files
- `mission-02-terminal/README.md` (this file)
- `terminal-practice/practice.txt`
- `terminal-practice/practice_renamed_backup.txt`

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
