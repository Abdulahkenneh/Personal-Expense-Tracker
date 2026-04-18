# Python Expense Tracker CLI

A command-line expense tracking application built to practice **file handling**, **data manipulation with pandas**, and **modular programming** in Python.

> 🧠 **Purpose:** This is a learning project created to understand CSV file operations, data persistence, and basic CRUD functionality before building larger applications. It is not intended for production use.

---

## 🎯 What I Learned

- Reading/writing CSV files with `pandas`
- Using global dictionaries for temporary data storage
- Structuring a CLI application with modular functions
- Basic input handling and user flow management
- Persisting data between sessions

---

## 📋 Features

| Feature | Description |
|---------|-------------|
| ➕ Add expenses | Record date, category, amount, and description |
| 👁️ View expenses | Display all expenses as a pandas DataFrame |
| 💰 Track budget | Set monthly budget and compare against total spending |
| 💾 Save to CSV | Persist expenses to `expenses.csv` |
| 📂 Load from CSV | Automatically load existing data on startup |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **pandas** — for DataFrame display and CSV handling
- **os** — file existence checking

---

## 🔧 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Abdulahkenneh/python-expense-tracker-cli.git
cd python-expense-tracker-cli
2. Install dependencies
bash
pip install pandas
3. Run the application
bash
python expense_tracker.py
4. Menu options
text
Choose an option:
1: Add expenses
2: View expenses
3: Track budget
4: Save expenses to CSV
5: Exit
📁 File Structure
text
python-expense-tracker-cli/
├── expense_tracker.py    # Main application
├── expenses.csv          # Auto-generated data file
└── README.md
🧪 Example Session
text
Enter your expense details:
Enter date (YYYY-MM-DD): 2026-04-18
Category of Expense (e.g., Food, Travel): Food
Enter the amount spent: 45.50
Please Enter a description: Groceries
Expense has been added successfully.

Choose an option:
1: Add expenses
2: View expenses
3: Track budget
4: Save expenses to CSV
5: Exit
Enter your choice: 2

Here are your current expenses:
   date_of_expensive category_of_expensive amount Description
0         2026-04-18                 Food   45.5   Groceries
🔮 Future Improvements (If I Revisit)
Input validation (prevent crashes on non-numeric amounts)

Edit/delete individual expenses

Visual summaries with matplotlib

Web interface with Streamlit

📚 Why I Built This
This project was a stepping stone before building larger applications like:

Full-Stack Education Platform

AI-Powered Data Analysis Tool

It helped me understand:

File persistence fundamentals

How to structure a CLI app

Basic pandas operations

👨‍💻 Author
Abdulah Mamadee Kenneh
GitHub | LinkedIn

📄 License
Educational use only. Not for production deployment.

text

---

---
