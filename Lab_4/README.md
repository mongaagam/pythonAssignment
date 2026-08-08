# Lab 4 - Command Line and Bash

## Objective

The objective of this lab is to practice Linux command-line tools and Bash scripting by downloading a text file, analyzing word frequency, and creating a reusable shell script.

---

## Files

- `1342-0.txt` - Downloaded text file
- `11-0.txt` - Second text file used for testing
- `top_words.sh` - Bash script to find the most frequent words
- `Check.txt` - Sample test file

---

## Commands Used

### Download a text file

```bash
curl -O https://www.gutenberg.org/files/1342/1342-0.txt
```

### Count lines, words, and characters

```bash
wc 1342-0.txt
```

### Find the top frequent words

```bash
tr '[:upper:]' '[:lower:]' < 1342-0.txt | tr -cs '[:alpha:]' '\n' | sort | uniq -c | sort -nr | head
```

---

## Bash Script

Run the script using:

```bash
./top_words.sh 1342-0.txt
```

To display a custom number of words:

```bash
./top_words.sh 1342-0.txt 15
```

---

## Output

The script displays the most frequently occurring words in the given text file.

Example:

```text
4665 the
4325 to
3846 of
3767 and
2284 her
2122 i
2038 a
1994 in
1875 was
1751 she
```

---

# Output

## Step 1: Downloading the Text File

The text file was downloaded successfully from Project Gutenberg using the `curl` command.

<img width="1470" height="96" alt="Screenshot 2026-08-08 at 6 00 54 PM" src="https://github.com/user-attachments/assets/f0f878a0-e0e7-4198-a354-bb1b0f7c2a1e" />

---

## Step 2: Finding the Top Frequent Words

The downloaded text file was analyzed using the `tr`, `sort`, `uniq`, and `head` commands to identify the top 10 most frequently occurring words.

<img width="1470" height="286" alt="Screenshot 2026-08-08 at 6 34 37 PM" src="https://github.com/user-attachments/assets/933597d4-345d-4352-b4c1-18a70ae8b80d" />


## Step 3: Counting Lines, Words, and Characters

The `wc` command was used to count the total number of lines, words, and characters in the downloaded text file (`1342-0.txt`).

The output shows:

- **14537** lines
- **127381** words
- **738046** characters

<img width="1470" height="44" alt="Screenshot 2026-08-08 at 6 14 43 PM" src="https://github.com/user-attachments/assets/bdb407b1-d151-4287-91c7-6c736608df01" />

---

## Step 4: Bash Script Implementation

A reusable Bash script named `top_words.sh` was created. The script accepts a text file as input, converts the text to lowercase, counts the frequency of each word, sorts the results, and displays the most frequent words automatically.

<img width="1470" height="192" alt="Screenshot 2026-08-08 at 6 01 58 PM" src="https://github.com/user-attachments/assets/19696ab5-29b4-4bf1-959c-f5f4943ecaac" />

---

## Step 5: Executing the Bash Script

The Bash script was executed successfully using the downloaded text file (`1342-0.txt`). The output displayed the most frequently occurring words in the file.

<img width="1467" height="262" alt="Screenshot 2026-08-08 at 6 42 05 PM" src="https://github.com/user-attachments/assets/1a916c6a-d1ad-45a2-8667-74c699343247" />


---

## Step 6: Testing the Script with a Custom File

A custom text file (`Check.txt`) was created to verify that the script works correctly with any text file. The script was executed using this file, and the output confirmed that the word frequencies were calculated correctly.

### Custom Input File (`Check.txt`)

<img width="1470" height="196" alt="Screenshot 2026-08-08 at 6 40 29 PM" src="https://github.com/user-attachments/assets/d553e647-ccdc-4a64-b29e-b49685563ffb" />


### Script Execution

<img width="1467" height="219" alt="Screenshot 2026-08-08 at 6 38 40 PM" src="https://github.com/user-attachments/assets/cf30b933-5136-4cbc-95bc-6b21cdc703c2" />

## Conclusion

In this lab, Linux command-line tools such as `curl`, `tr`, `sort`, `uniq`, `head`, and `wc` were used to analyze a text file. A reusable Bash script (`top_words.sh`) was created to automate the process of finding the most frequent words from any text file. The script was successfully tested using both the downloaded text file and a custom text file.
