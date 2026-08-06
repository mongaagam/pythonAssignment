# Lab 2 - Python Assignment

## Overview
This lab demonstrates basic Python programming concepts including:
- Word frequency counting
- Using Counter from collections
- Flattening nested lists
- File handling
- Exception handling
- List Comprehension
- Generator explanation

---

## Project Structure

```text
lab_2/
│── lab2.py
│── number.txt
│── README.md
│── .gitignore
│── requirements.txt
```

---

## Question 1 - Word Count

Count the frequency of each word in a sentence.

Example Input:

```
Hello, hello World!
```

Output:

```
{'hello': 2, 'world': 1}
```

---

## Question 2 - Counter

Use Python's built-in `Counter` class to count word frequencies.

Example Output:

```
Counter({'hello': 2, 'world': 1})
```

---

## Question 3 - Flatten Nested List

Flatten a list of lists using:

- Normal Loop
- List Comprehension

Input:

```
[[1,2],[3,4],[5]]
```

Output:

```
[1,2,3,4,5]
```

---

## Question 4 - Mean of File

Create a file named `number.txt`.

Content:

```
1
agam
2
3
5
abc
```

The program:

- Reads the file
- Ignores invalid values like `abc`
- Calculates the average of valid numbers

Output:

```
2.75
```

---

## Question 5

Difference between List Comprehension and Generator Expression.

- List Comprehension creates the complete list in memory.
- Generator Expression creates values one by one and uses less memory.

---

## Question 6

Test all functions using:

```python
if __name__ == "__main__":
```

If `number.txt` is missing, display:

```
File not found
```

instead of crashing.

---

## How to Run

Run the program using:

```bash
python3 lab2.py
```

---

## Sample Output

```
Q1:
{'hello': 2, 'world': 1}

Q2:
Counter({'hello': 2, 'world': 1})

Q3 (Using Loop):
[1, 2, 3, 4, 5]

Q3 (Using List Comprehension):
[1, 2, 3, 4, 5]

Q4:
2.75
```

---

## Screenshots

### Create Files

<img width="1470" alt="Create File" src="https://github.com/user-attachments/assets/793b717f-6ac4-4e61-9bbd-d289b53bfe15">

---

### number.txt Content

<img width="1470" alt="number.txt" src="https://github.com/user-attachments/assets/c8227cfe-0907-467a-a2cd-e2f42ab31cea">

---

### Source Code (Part 1)

<img width="1470" alt="Code 1" src="https://github.com/user-attachments/assets/3c2df6a3-c3fb-4f2c-b294-cba8031b5f6d">

---

### Source Code (Part 2)

<img width="1470" alt="Code 2" src="https://github.com/user-attachments/assets/7914c3cb-3b79-485d-9cda-8269a53e81cf">

---

### Source Code (Part 3)

<img width="1470" alt="Code 3" src="https://github.com/user-attachments/assets/489c7504-5998-4985-8b41-fb64e42c4b6a">

---

### Source Code (Part 4)

<img width="1470" alt="Code 4" src="https://github.com/user-attachments/assets/88ac7eaf-e141-4e92-8c8c-439c7b4efb15">

---

### Source Code (Part 5)

<img width="1470" alt="Code 5" src="https://github.com/user-attachments/assets/4f4ae3c7-2ba5-4c22-964a-c8620df16908">

---

### Source Code (Part 6)

<img width="1470" alt="Output" src="https://github.com/user-attachments/assets/fb999cb6-e130-46a9-812d-23728ffaff26">

---

## Sample Output

<img width="1468" height="463" alt="Screenshot 2026-08-06 at 1 40 34 PM" src="https://github.com/user-attachments/assets/1ca78485-2072-4263-aada-73f1cf4f633c" />


