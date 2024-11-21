# budget_tracker.py

import json

# File to save the data
DATA_FILE = "budget_data.json"

# Load data from file or initialize a new dataset
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"transactions": []}  # Return an empty dataset if file doesn't exist

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a transaction (income/expense)
def add_transaction(data, amount, description):
    transaction = {
        "amount": amount,
        "description": description,
        "type": "Income" if amount > 0 else "Expense"
    }
    data["transactions"].append(transaction)
    save_data(data)

# Calculate total balance
def calculate_balance(data):
    return sum(t["amount"] for t in data["transactions"])

# Generate a simple report
def generate_report(data):
    income = sum(t["amount"] for t in data["transactions"] if t["amount"] > 0)
    expenses = sum(-t["amount"] for t in data["transactions"] if t["amount"] < 0)
    balance = calculate_balance(data)
    print("\n--- Budget Report ---")
    print(f"Total Income: ₹{income}")
    print(f"Total Expenses: ₹{expenses}")
    print(f"Balance: ₹{balance}")

# Main Menu
def main():
    data = load_data()
    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: ₹"))
            description = input("Enter income description: ")
            add_transaction(data, amount, description)
            print("Income added successfully.")
        elif choice == "2":
            amount = float(input("Enter expense amount: ₹"))
            description = input("Enter expense description: ")
            add_transaction(data, -amount, description)  # Expenses are negative
            print("Expense added successfully.")
        elif choice == "3":
            generate_report(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
