# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 was to understand how data and numbers are represented inside computers:
- Perform manual conversions between Decimal (base 10), Binary (base 2), and Hexadecimal (base 16) by hand showing all steps.
- Verify the manual answers using Python's built-in conversion functions (`bin()`, `hex()`, and `int()`).
- Write an interactive Python number converter (`number_converter.py`) that converts user-provided decimal numbers into binary and hex.
- Explore character encoding standards (ASCII and UTF-8) and explain how text characters are stored digitally.

---

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | **Successive division by 2:**<br>• $13 \div 2 = 6$, remainder **1**<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1**<br>Read remainders from bottom to top: **$1101_2$**<br>*(Verification: $8 + 4 + 0 + 1 = 13$)* |
| **Convert decimal 25 to binary.** | **Successive division by 2:**<br>• $25 \div 2 = 12$, remainder **1**<br>• $12 \div 2 = 6$, remainder **0**<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1**<br>Read remainders from bottom to top: **$11001_2$**<br>*(Verification: $16 + 8 + 0 + 0 + 1 = 25$)* |
| **Convert binary 1010 to decimal.** | **Positional expansion:**<br>• $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>• $(1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$<br>• $8 + 0 + 2 + 0 = \mathbf{10_{10}}$ |
| **Convert binary 1101 to decimal.** | **Positional expansion:**<br>• $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>• $(1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$<br>• $8 + 4 + 0 + 1 = \mathbf{13_{10}}$ |
| **Convert hexadecimal A to decimal.** | **Positional expansion in base 16:**<br>• $A \times 16^0$<br>In hexadecimal, $A$ represents $10$.<br>• $10 \times 1 = \mathbf{10_{10}}$ |
| **Convert hexadecimal 1F to decimal.** | **Positional expansion in base 16:**<br>• $(1 \times 16^1) + (F \times 16^0)$<br>Since $F = 15$ in hexadecimal:<br>• $(1 \times 16) + (15 \times 1) = 16 + 15 = \mathbf{31_{10}}$ |
| **Convert binary 1111 to hexadecimal.** | **4-bit grouping:**<br>• Positional sum: $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 15_{10}$<br>In base 16, value 15 is represented by single digit **$\mathbf{F_{16}}$** (or `0xF`). |

---

### Task 5.2 — Verify using Python
Tested inside the Python 3 interactive shell:

| Test expression | Result in Python | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes, matches $1101_2$. |
| `bin(25)` | `'0b11001'` | Yes, matches $11001_2$. |
| `int('1010', 2)` | `10` | Yes, matches $10_{10}$. |
| `int('1101', 2)` | `13` | Yes, matches $13_{10}$. |
| `int('A', 16)` | `10` | Yes, matches $10_{10}$. |
| `int('1F', 16)` | `31` | Yes, matches $31_{10}$. |
| `hex(0b1111)` | `'0xf'` | Yes, matches $F_{16}$. |

---

### Task 5.3 — Build a small number converter
Created `number_converter.py` which takes decimal input, converts it using `bin()` and `hex()`, and prints the results cleanly.

#### Test Results:
| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **42** | `0b101010` (raw: `101010`) | `0x2a` (uppercase: `2A`) |
| **255** | `0b11111111` (raw: `11111111`) | `0xff` (uppercase: `FF`) |
| **1024** | `0b10000000000` (raw: `10000000000`) | `0x400` (uppercase: `400`) |

#### Explanation of Python conversion functions:
- `bin(x)`: Takes an integer $x$ and returns its binary string representation prefixed with `'0b'` (e.g. `bin(42)` $\to$ `'0b101010'`).
- `hex(x)`: Takes an integer $x$ and returns its lowercase hexadecimal string representation prefixed with `'0x'` (e.g. `hex(255)` $\to$ `'0xff'`).
- `int(string, base)`: Converts a string of digits in a given base (like base 2 or base 16) back into a standard base-10 integer.

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase letter **'A'**: ASCII decimal code **`65`** (Binary: `01000001`).
  - Lowercase letter **'a'**: ASCII decimal code **`97`** (Binary: `01100001`).
  *(Notice there is a constant difference of 32 between uppercase and lowercase ASCII letters, which corresponds to bit 5 being toggled).*
- **Why computers need an encoding standard:**
  Computers cannot directly store symbols or alphabets because silicon transistors only recognize electrical on/off states (0 and 1). An encoding standard creates an agreed-upon numerical table assigning a specific binary number to every letter, punctuation mark, and digit so that all computers, operating systems, and programs display the exact same characters.
- **Example of a character not in basic ASCII:**
  The Indian Rupee currency sign **`₹`** (Unicode code point `U+20B9`), or an emoji like **`👍`**. Basic ASCII is only a 7-bit standard supporting 128 characters, so modern systems use **UTF-8** (Unicode) to support thousands of characters from all world languages and symbols.

---

## 3. Commands / tools used
- `python3 -i`: Ran interactive Python to test conversion functions (`bin()`, `hex()`, `int()`, `ord()`).
- `python3 number_converter.py`: Executed the script from terminal and tested with various integer inputs.
- `cat number_converter.py`: Verified file contents.

## 4. My understanding
- Binary is base 2 because computer memory is built of electronic switches (transistors) that are either ON (1) or OFF (0).
- Hexadecimal is base 16 and is extremely popular in computing because exactly 4 binary bits equal 1 hexadecimal digit ($2^4 = 16$). This makes large binary numbers much shorter and easier for programmers to read (e.g. `11111111` is just `FF`).
- Characters in text files are literally just numbers mapped through encoding tables like ASCII or UTF-8.

## 5. Difficulties faced
- In `number_converter.py`, if a user types letters or leaves the input blank, `int(user_input)` raises a `ValueError` crash.
- Also, `bin()` and `hex()` return strings starting with prefixes `0b` and `0x`, which can look confusing if you only want the raw digits.

## 6. How I resolved them
- I wrapped the integer parsing inside a `try...except ValueError` block to handle invalid inputs gracefully.
- I used string slicing (`[2:]`) to display both the standard Python prefixed format and the clean raw digits.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`
- `mission-05-numbers-data/README.md` (this file)

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Branch:** `main`
- **Pushed to GitHub:** Yes
