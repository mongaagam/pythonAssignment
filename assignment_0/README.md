# Assignment 0

## Problem Statement

The objective of this assignment is to create a Python program that demonstrates the use of Python 3.11 features but not in 3.8.

The program should:

- Take a number as input from the user.
- Print the multiplication table of the entered number from 1 to 10.
- Demonstrate the use of `ExceptionGroup`.
- Handle the exception using `except*`.

---

## Python Version

- Python 3.11.13
- Python 3.8.20
---

## Files

```
AssignmentsZero/
├── assignment_0.py
└── .gitignore
```

---

## Code

```python
a = int(input("Enter a number : "))
print(f"Multiplication table of {a} :")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")

    raise ExceptionGroup(
        "Errors",
        [ValueError("Wrong Value")]
    )

except* ValueError:
    print("Exception handle")
```

---

## Explanation

### Input

The program takes a number from the user using the `input()` function.

### Multiplication Table

A `for` loop is used to print the multiplication table from 1 to 10.

### ExceptionGroup

An `ExceptionGroup` is created to demonstrate the new feature introduced in Python 3.11.

### except*

The `except*` statement catches the `ValueError` inside the exception group.

---

## Output

The program prints:

- Multiplication table of the entered number.
- Exception handling message.

---


# Screenshots

## 1. Running the program in Python 3.11

This screenshot shows the successful execution of the program using Python 3.11.13.

<img width="1470" height="364" alt="Screenshot 2026-08-05 at 6 23 18 PM" src="https://github.com/user-attachments/assets/6edf0127-0736-496b-8d9e-59c2291bbc02" />

---

## 2. Multiplication Table Output

This screenshot shows the multiplication table generated for the entered number.

<img width="1470" height="956" alt="Screenshot 2026-08-05 at 6 24 12 PM" src="https://github.com/user-attachments/assets/4ce18b8c-3f37-4f55-89d6-ae2ab95c3047" />

---

## 3. ExceptionGroup Demonstration

This screenshot demonstrates the use of the `ExceptionGroup` feature introduced in Python 3.11.

<img width="1470" height="457" alt="Screenshot 2026-08-05 at 6 24 27 PM" src="https://github.com/user-attachments/assets/1e4f8dd4-b8d0-43da-9516-83bff8ef0c61" />

---

## 4. Exception Handling using `except*`

This screenshot shows how the `except*` statement catches the `ValueError` from the `ExceptionGroup`.

<img width="1470" height="265" alt="Screenshot 2026-08-05 at 6 25 22 PM" src="https://github.com/user-attachments/assets/61ae65e4-bc09-4900-8bb1-1973b97ad14b" />

