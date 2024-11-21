Description: Command-Line Budget Tracker

The Budget Tracker application is a Python-based command-line program designed to help you efficiently manage and track your income, expenses, and overall financial balance. It is user-friendly, supports persistent data storage, and generates reports to provide a quick overview of your financial health. 

---

Features
1. Persistent Storage:
   - All transaction data (income and expenses) is saved to a file (`budget_data.json`).
   - Ensures data is retained even after the application is closed.

2. Simple and Intuitive Menu:
   - The menu offers four straightforward options:  
     - Add Income  
     - Add Expense  
     - View Report  
     - Exit  

3. Detailed Financial Report:
   - View total income, total expenses, and current balance.
   - The report helps you analyze your financial situation effectively.

4. Categorized Transactions:
   - Transactions are labeled as Income (positive amounts) or Expense (negative amounts).

---
How It Works
1. Adding Income:
   - Enter the amount and a description for the income source.
   - The app adds the transaction to your records as an Income.

2. Adding Expenses:
   - Enter the amount and a description for the expense.
   - Expenses are stored as negative amounts.

3. Viewing Reports:
   - The report shows:
     - Total Income
     - Total Expenses
     - Balance (calculated as income minus expenses).

4. Saving Data:
   - All transactions are saved in `budget_data.json` for future reference.

---
Technical Details
1. Programming Language: Python
2. File-Based Storage: 
   - Data is stored in a local JSON file (`budget_data.json`).
   - The file is created automatically if it does not exist.
3. Functions:
   - load_data(): Loads transaction data from the JSON file.
   - save_data(data): Saves updated data back to the file.
   - add_transaction(data, amount, description): Adds a transaction (income or expense).
   - calculate_balance(data): Calculates the current financial balance.
   - generate_report(data): Prints a financial summary.

---
Usage Instructions
1. Setup:
   - Ensure Python is installed on your system.
   - Open VS Code and create a new file named `budget_tracker.py`.
   - Copy the provided code into this file.

2. Running the Application:
   - Open the terminal in VS Code (`Ctrl + ``) and navigate to the script's directory.
   - Run the application:
     ```bash
     python budget_tracker.py
     ```

3. Interacting with the Menu:
   - Option 1: Add an income with a description.
   - Option 2: Add an expense with a description.
   - Option 3: View a report summarizing your financial details.
   - Option 4: Exit the application.

---

Benefits
- Helps track finances easily from the command line.
- Saves time with a simple interface.
- Provides insights into spending habits and current balance.
