# 💰 Expense Tracker CLI

> A clean, minimal, and scalable command-line Expense Tracker built using Python and OOP principles.

---

## 🚀 Features

- 🧾 Add expenses via user input  
- 📂 Store expenses in CSV format  
- 📅 Strict Date Validation (`YYYY-MM-DD`)  
- 🔒 Category & Amount Validation  
- 🧠 Object-Oriented Design  
- ⚡ Lightweight and beginner-friendly  
- 🛠️ Clean Architecture (Separation of Concerns)

---

## 📁 Project Structure

---

## 🧠 How It Works

### 1️⃣ `expense.py`

Defines the `Expense` class:

- Stores:
  - `amount`
  - `category`
  - `date`
  - `description`

- Includes:
  - `@classmethod from_input()` → Creates object from user input
  - `__str__()` → Clean string representation
  - `VALID_CATEGORIES` set → Prevents invalid category entries

---

### 2️⃣ `file_manager.py`

Handles:

- Input validation
- Date format validation using `datetime`
- CSV writing using `csv` module
- Proper exception handling
- Clean program flow using `main()` function

---

## 🔐 Validation Rules

✔ Amount must be **greater than 0**  
✔ Category must be one of:


✔ Date must follow:


If any rule fails → Program raises a clear error message.

---

## 🖥️ Example Usage


Output: To be added Soon

If invalid input: To be added Soon


---

## 📊 Stored CSV Format

| Amount | Category | Date | Description |
|--------|----------|------|-------------|
| 250 | Food | 2026-02-22 | Lunch with friends |

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 📦 Built-in `csv` module
- 📅 Built-in `datetime` module
- 🧠 Object-Oriented Programming (OOP)

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker

python file_manager.py
