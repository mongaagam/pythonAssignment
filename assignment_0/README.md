Assignment 0
Problem Statement
The objective of this assignment is to create a Python program that uses Python 3.11 features and runs successfully in Python 3.11 but not in Python 3.8.

The program should:

Take a number as input from the user.
Print the multiplication table of the entered number from 1 to 10.
Demonstrate the use of ExceptionGroup.
Handle the exception using except*.
Python Version
Python 3.11.13

Python 3.8.20

Files
AssignmentsZero/
├── assignment_0.py
└── .gitignore
Code
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
Explanation
Input
The program takes a number from the user using the input() function.

Multiplication Table
A for loop is used to print the multiplication table from 1 to 10.

ExceptionGroup
An ExceptionGroup is created to demonstrate the new feature introduced in Python 3.11.

except*
The except* statement catches the ValueError inside the exception group.

Output
The program prints:

Multiplication table of the entered number.
Exception handling message.
Screenshots
1. Creating the Python File
This screenshot shows the creation of the assignment_0.py file in the project directory.

Screenshot 2026-08-05 at 6 23 18 PM
2. Python Program
This screenshot shows the Python program written in assignment_0.py. The program prints the multiplication table of a number and demonstrates the use of the Python 3.11 features ExceptionGroup and except*.

Screenshot 2026-08-05 at 6 24 12 PM
3. Running the Program in Python 3.11
This screenshot shows that the program executes successfully using Python 3.11.13, as ExceptionGroup and except* are supported in Python 3.11.

Screenshot 2026-08-05 at 6 24 27 PM ---
4. Running the Program in Python 3.8
This screenshot shows that the same program does not run in Python 3.8.20 because ExceptionGroup and except* are Python 3.11 features and are not available in Python 3.8.

Screenshot 2026-08-05 at 6 25 22 PM
