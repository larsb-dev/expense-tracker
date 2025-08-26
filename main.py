from csv import DictReader, DictWriter
import csv
import datetime
import os
import textwrap

from tabulate import tabulate

def load_expenses():
    expenses = []
    with open("expenses.csv", "r", encoding="utf-8", newline="") as csvfile:
        reader = DictReader(csvfile, delimiter=',')
        for row in reader:
            expenses.append(row)
    return expenses

def get_previous_id(expenses):
    return expenses[-1]["id"]

def add_expense():
    if not load_expenses():
        id = 1
    else:
        id = get_previous_id(load_expenses()) + 1

    date = datetime.date.today().isoformat()
    category = input("What expense category do you wish to add? ")
    description = input("What expense do you wish to add? ")

    while True:
        try:
            amount = float(input("What amount do you wish to add? "))
            break
        except ValueError:
            print("Please enter a valid number for amount.")

    expense = {
        "id": id,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    filename = "expenses.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, "a", encoding="utf-8", newline="") as csvfile:
        fieldnames = ['date', 'category', 'description', 'amount']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()
        writer.writerow(expense)

def sum_expenses(expenses):
    total = 0
    for expense in expenses:
        total += float(expense["amount"])
    return total

def print_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return
    headers = ["date", "category", "description", "amount"]
    rows = [[expense["date"], expense["category"], expense["description"], expense["amount"]] for expense in expenses]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def list_all_expenses(expenses):
    print_expenses(expenses)

def list_expenses_by_category(expenses, category):
    if not category:
        print_expenses(expenses)
    else:
        filtered = [expense for expense in expenses if expense["category"].lower() in category.lower()]
        print_expenses(filtered)

def main():
    end = False
    while not end:
        try:
            print(textwrap.dedent(
            f"""\
            {"*" * 33}
            Welcome to the Expense Tracker 🤑\n
            Options to chose from:
            1. Add an expense
            2. List all expenses
            3. List all expenses by category
            4. Edit an expense
            5. Delete an expense
            6. Exit the app
            {"*" * 33}
            """))
            choice = input("What would you like to do? ")
            match choice:
                case "1":
                    print_expenses(load_expenses("expenses.csv"))
                case "2":
                    add_expense()
                case "3":
                    summary = sum_expenses(load_expenses("expenses.csv"))
                    print(summary)
                case "4":
                    end = True
        except FileNotFoundError:
            print("No expenses found")

if __name__ == "__main__":
    main()