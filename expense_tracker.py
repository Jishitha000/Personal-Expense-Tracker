# expense_tracker.py

import json
from datetime import datetime

class Expense:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date
        }
def save_expenses(expenses):
    """Saves the list of expenses to a JSON file."""
    with open('expenses.json', 'w') as f:
        json.dump([expense.to_dict() for expense in expenses], f, indent=4)

def load_expenses():
    """Loads expenses from a JSON file and returns a list of Expense objects."""
    try:
        with open('expenses.json', 'r') as f:
            return [Expense(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading expenses. The file may be corrupted.")
        return []
def add_expense(expenses):
    """Adds a new expense to the list."""
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    expenses.append(Expense(amount, category, date))
    print("Expense added.")

def view_summary(expenses):
    """Displays a summary of expenses."""
    total_spending = sum(exp.amount for exp in expenses)
    print(f"\nTotal Spending: ${total_spending:.2f}")

    category_summary = {}
    for expense in expenses:
        if expense.category in category_summary:
            category_summary[expense.category] += expense.amount
        else:
            category_summary[expense.category] = expense.amount

    print("\nSpending by Category:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            save_expenses(expenses)
            print("Expenses saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
