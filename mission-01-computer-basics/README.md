# Mission 1 — Computer fundamentals and IPOS

## 1. Task / objective
The goal of this mission was to understand the core foundation of how computers work:
- Trace a real-world computing activity through the IPOS cycle (Input, Processing, Output, Storage).
- Identify and classify common hardware components and different types of software (Operating System, Application, and Utility).
- Examine computer-based systems used in everyday life outside of regular personal computers and phones.

---

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Writing and saving a Python script in a text editor (e.g., VS Code).

| Stage | What happens in my example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | I type lines of Python code using my keyboard and use the trackpad to navigate lines or click "Save". Keystroke electrical signals are sent to the computer. | Keyboard, Trackpad / Mouse |
| **Processing** | The CPU interprets each keystroke via OS interrupts, encodes characters into ASCII/Unicode binary values, and holds the active document buffer in volatile RAM. | CPU (Apple Silicon) and RAM |
| **Output** | The editor renders the typed text onto the display monitor in real time so I can visually see what I wrote. A small indicator shows if there are unsaved changes. | Retina Display / Screen |
| **Storage** | When I press `Cmd + S` (Save), the operating system copies the file data from temporary RAM onto the non-volatile solid state drive as a permanent `.py` file. | 512GB Apple SSD (Solid State Drive) |

**Flow of the activity:**
The activity begins with user interaction through input devices (keyboard/trackpad). These actions trigger electrical signals that the CPU handles immediately in temporary memory (RAM). The CPU coordinates with the graphics processor to produce visual output on the screen so the user gets instant visual feedback. Finally, when saved, the file data is transferred from volatile RAM down to persistent storage (SSD), so it is not lost when the computer shuts down.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Keyboard** | Hardware | Not applicable | Used to enter text, commands, and code into the computer. |
| **Retina Screen / Monitor** | Hardware | Not applicable | Displays visual output, windows, and graphical user interfaces. |
| **Solid State Drive (SSD)** | Hardware | Not applicable | Provides permanent, non-volatile storage for files and installed applications. |
| **RAM (Unified Memory)** | Hardware | Not applicable | Provides fast, temporary working memory for active programs and the OS. |
| **macOS** | Software | Operating system software | Manages computer hardware, controls process execution, and coordinates files. |
| **Visual Studio Code** | Software | Application software | Text editor used for writing code, editing files, and debugging programs. |
| **Google Chrome** | Software | Application software | Web browser used for accessing online resources, research, and documentation. |
| **Activity Monitor** | Software | Utility software | System maintenance tool that monitors running processes, RAM, and CPU usage. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Allows bank customers to withdraw cash, check balances, and transfer funds safely without visiting a bank branch. | Keypad / PIN entry and Card reader | Cash dispenser mechanism and printed receipt / screen prompt |
| **Metro Station Ticket Vending Machine** | Sells single-journey tokens or recharges travel smart cards for metro commuters. | Touchscreen selection and currency / UPI scanner | Dispensed plastic token / updated smart card and printed receipt |
| **Smart Traffic Light System** | Manages vehicular traffic flow and pedestrian crossing times based on road congestion. | Infrared vehicle sensor or pedestrian push button | Colored signal lights (Red, Yellow, Green) and countdown timer |

---

## 3. Commands / tools used
- Text Editor (VS Code) to format and write the notes and tables in Markdown.
- Activity Monitor (macOS utility) to verify hardware specs and see RAM/CPU utilization.

## 4. My understanding
- **IPOS Cycle:** Every computer, whether a laptop, phone, or microwave controller, works on the IPOS model. Input is taking raw data in, processing is converting or computing that data using the CPU and RAM, output is showing the result to a human or machine, and storage is preserving the information permanently.
- **Hardware vs. Software:** Hardware is the physical physical silicon, wires, and casing that you can touch. Software is the set of digital instructions that tell the hardware what to do.
- **Software Categories:**
  - *Operating System Software* (like macOS, Linux, Windows) sits directly on the hardware and acts as the manager.
  - *Application Software* (like VS Code, Chrome) helps the user perform specific work tasks.
  - *Utility Software* (like Activity Monitor, Disk Utility, antivirus) helps support, tune, and protect the system itself.

## 5. Difficulties faced
- Initially, it was easy to confuse RAM with Storage because both store data. I had to remind myself that RAM is volatile (cleared when powered off) and super fast, while the SSD is non-volatile (holds files permanently) but slower than RAM.

## 6. How I resolved them
- I observed what happens when I type without saving: if the application crashes before saving, the unsaved buffer in RAM is gone. Once saved to disk, the file persists across reboots. This made the distinction between Processing/RAM and Storage clear.

## 7. Evidence / files
- `mission-01-computer-basics/README.md` (this file with all 3 completed tables).

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
