# Lab 3 – Git and GitHub Workflow

## Objective

The objective of this lab was to practice the complete Git and GitHub workflow using the code developed in **Lab 2**.

---

# Changes Made

For this lab, no new Python functionality was implemented.

The existing **Lab 2 code** (`lab_2/lab2.py`) was used to practice the complete Git workflow.

The following tasks were completed:

- Created a feature branch `feature/word-count`.
- Added the Lab 2 implementation through multiple meaningful commits.
- Pushed the feature branch to GitHub.
- Created a Pull Request from `feature/word-count` to `main`.
- Added reviewers for peer review.
- Addressed the review feedback by creating a follow-up commit.
- Created a review-fix Pull Request.
- Merged the Pull Request into the `main` branch.
- Deleted the feature branch after merging.
- Removed the duplicate `number.txt` file from the repository.
- Verified that the repository was clean.

---

# Git Commands Used

```bash
git checkout -b feature/word-count
git add .
git commit -m "add word_count function"
git commit -m "add word_count_counter function"
git commit -m "add flatten functions"
git commit -m "complete Lab 2 assignment"
git push origin feature/word-count

git checkout -b feature/review-fix
git commit -m "address peer review feedback"
git push -u origin feature/review-fix

git branch
git log --oneline -5
git status
```

---

# Screenshots

## 1. Git Branches

<img width="1470" height="72" alt="Screenshot 2026-08-07 at 5 44 31 PM" src="https://github.com/user-attachments/assets/e7279d89-3c5a-40cd-bc54-0c56e818d08f" />


## 2. Git Commit History

The screenshot below shows the commit history for the feature branch. The Lab 2 implementation was added through multiple meaningful commits as part of the Lab 3 Git workflow.

<img width="1470" height="140" alt="Screenshot 2026-08-07 at 5 46 20 PM" src="https://github.com/user-attachments/assets/7d103ac1-f410-495a-ad38-2563f804d6a2" />


## 3. Peer Review and Follow-up Changes

A peer review was requested on the Pull Request. The reviewer suggested adding a docstring at the top of the file.

The requested change was implemented, a follow-up commit was created, and the reviewer confirmed that the issue had been resolved.

**Reviewer Feedback:**
> Add a docstring at the top of main.py

**Response:**
> Done

**Reviewer Confirmation:**
> Ok, thank you

<img width="1464" height="598" alt="Screenshot 2026-08-07 at 5 47 47 PM" src="https://github.com/user-attachments/assets/91557ee6-11bf-45a7-8ecb-97861248bf2d" />


## 4. Pull Request Merged

After completing the development work and resolving the peer review feedback, the Pull Request was successfully merged into the **main** branch. This completed the Git and GitHub workflow for Lab 3.

**Activities completed:**
- Created a feature branch
- Added multiple meaningful commits
- Created a Pull Request
- Requested peer review
- Addressed the review feedback
- Successfully merged the Pull Request into the `main` branch

<img width="1463" height="684" alt="Screenshot 2026-08-07 at 5 48 15 PM" src="https://github.com/user-attachments/assets/b88b1dcc-8f77-4f6a-b54a-d4653d9de37c" />


# Learning Outcomes

- Learned how to create and use feature branches.
- Learned how to make multiple meaningful commits.
- Learned how to push changes to GitHub.
- Learned how to create Pull Requests.
- Learned how to request and address peer reviews.
- Learned how to create follow-up commits.
- Learned how to merge Pull Requests.
- Learned how to manage and clean up Git branches.
- Understood the complete GitHub workflow using the Lab 2 implementation.
