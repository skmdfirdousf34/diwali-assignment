# Mission 4 — How programs run

## 1. Task / objective
The goal of Mission 4 was to understand how computer programs are translated and executed by the machine:
- Create and run a basic Python program (`hello.py`) from the Terminal.
- Compare the two primary program translation approaches: Compilers vs. Interpreters.
- Explain the key differences between them in plain words using a comparison table.

---

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created a file named `hello.py` inside `mission-04-programs/`.
- Wrote a single line of Python code:
  ```python
  print("Hello from Python")
  ```
- Executed the script from the Terminal using:
  ```bash
  python3 hello.py
  ```
- **Observed output:**
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the whole source code into machine code all at once before the program can run. | Translates and executes the source code line by line (instruction by instruction) at runtime. |
| **Typical output** | Produces a separate, standalone machine executable file (like `.exe`, `.out`, or Mach-O binary). | Does not produce a separate standalone machine code binary; executes instructions directly in memory. |
| **One example** | C, C++, Rust, Go | Python, JavaScript, Ruby |
| **One advantage** | Runs much faster and more efficiently once compiled because the CPU executes native machine instructions directly. | Much easier to test and debug because errors are flagged on the exact line being executed without needing a rebuild step. |

#### Explanation of Difference:
A compiler and an interpreter are both language translators, but they operate at different times. A compiler takes the entire source code file written by a programmer and translates it into native machine code (binary 0s and 1s that the CPU hardware understands) before the program ever runs, producing a standalone executable file. In contrast, an interpreter reads the source code line by line at runtime, translating each instruction and carrying it out immediately. Because compiled programs are already in machine code, languages like C++ run significantly faster than interpreted languages like Python, but interpreted languages allow for interactive testing and cross-platform flexibility without recompilation.

---

## 3. Commands / tools used
- `python3 hello.py`: Invoked the Python 3 interpreter to read, compile to bytecode, and execute `hello.py`.
- `cat hello.py`: Checked the code inside the file from terminal.

## 4. My understanding
- Computers cannot directly understand human-readable high-level code like `print("...")`. The CPU only executes low-level machine instructions.
- A compiler does all the heavy translation upfront. If there is a syntax error anywhere in the file, it refuses to generate the executable.
- An interpreter processes code dynamically. It can run lines of code up until it hits an error line, which makes it great for learning and quick scripting.
- Python actually uses a hybrid approach: it compiles Python source code into intermediate bytecode (`.pyc`), which the Python Virtual Machine (PVM) then interprets.

## 5. Difficulties faced
- Initially, on macOS, typing `python hello.py` gave a "command not found" error because modern macOS doesn't alias `python` to `python3` by default.

## 6. How I resolved them
- I explicitly ran `python3 hello.py` instead of `python`, which correctly targeted the installed Python 3.14.7 interpreter.

## 7. Evidence / files
- `mission-04-programs/hello.py`
- `mission-04-programs/README.md` (this file)

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
