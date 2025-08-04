# Calculator CLI Tool

A simple and interactive command-line calculator built with Python. This tool allows users to perform basic arithmetic operations including addition, subtraction, multiplication, and division. It supports multiple aliases for commands to enhance user experience.

---

## Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* ⏹ Exit Option
* Accepts both numeric and text-based commands (e.g., `1`, `add`, `addition`)
* Continuous loop until exit
* Input validation with friendly prompts

---

## Getting Started

### Prerequisites

* Python 3.x installed on your system

### Running the Program

1. Clone the repository or download the `calculator.py` file.

2. Open your terminal and navigate to the directory containing `calculator.py`

3. Run the script:

```bash
python calculator.py
```

---

## Usage

You will be prompted to select an operation:

```
Select operation:
1. Add (add, addition)
2. Subtract (sub, subtract)
3. Multiply (mul, multiply)
4. Divide (div, divide)
5. Exit (exit)
```

Then:

* Enter your choice
* Input the two numbers when prompted
* View the result

### Example

```
Enter choice : multiply
Enter first number : 6
Enter second number : 7
Result: 42.0
```

```
Enter choice : exit
! Thank you !
```

---

## File Structure

```
calculator.py
README.md
```

---

## Future Improvements

* Add exception handling for division by zero
* Support more complex operations (e.g., square root, exponentiation)
* Create a GUI version using Tkinter or PyQt

---

## Author

Made with ❤️ by Radhe Tare
