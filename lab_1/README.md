# Lab 1

## Objective

The objective of this lab is to create a reproducible Python project using a virtual environment. The project demonstrates how to isolate project dependencies, create the required project files, and execute a Python program in a clean environment.

---

## Project Structure

```
lab_1/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Files

- **main.py** – Contains the Python program.
- **README.md** – Documentation of the project.
- **requirements.txt** – Stores the project dependencies.
- **.gitignore** – Prevents unnecessary files from being tracked by Git.

---

## How to Run

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 3. Run the Program

```bash
python main.py
```

---

## Output

The program prints:

- Name: Agam Monga
- Active Python Version

---

# Screenshots

## 1. Creating the Project

This screenshot shows the creation of the Lab 1 project and the required files.

<img width="1040" height="106" alt="Screenshot 2026-08-05 at 7 26 51 PM" src="https://github.com/user-attachments/assets/7c0a9291-b079-4a6a-b19f-444946be4305" />

<img width="1222" height="224" alt="Screenshot 2026-08-05 at 7 30 24 PM" src="https://github.com/user-attachments/assets/06074497-7015-453a-9b70-456d7a1da4bd" />

---

## 2. Python Program
<img width="1030" height="83" alt="Screenshot 2026-08-05 at 7 31 43 PM" src="https://github.com/user-attachments/assets/0f71783d-41b1-4c79-be21-5a9215541279" />

## 3. Running the Program

This screenshot shows the successful execution of the program inside the virtual environment.

<img width="952" height="68" alt="Screenshot 2026-08-05 at 7 28 00 PM" src="https://github.com/user-attachments/assets/7a59a5b6-afe6-4532-8fae-9de378edd3b9" />


---

## 4. Generating requirements.txt

This screenshot shows the creation of the `requirements.txt` file using:

```bash
pip freeze > requirements.txt
```

<img width="1324" height="36" alt="Screenshot 2026-08-05 at 7 32 16 PM" src="https://github.com/user-attachments/assets/c41c1f22-f08c-4fc5-93bc-2223318f2a19" />

---

## Conclusion

This lab demonstrates how to:

- Create a Python project.
- Create and activate a virtual environment.
- Execute a Python program.
- Generate a `requirements.txt` file.
- Organize the project using Git and GitHub.
