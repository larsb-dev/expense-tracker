import csv
import datetime
import textwrap

from expense_tracker import *

def load_expenses(filename):
    expenses = []
    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = DictReader(csvfile, delimiter=',')
        for row in reader:
            expenses.append(row)
    return expenses

def add_expense():
    date = datetime.date.today().isoformat()
    category = input("What category do you wish to add? ")
    description = input("What description do you wish to add? ")
    amount = input("What amount do you wish to add? ")

    expense = {"date": date, "category": category, "description": description, "amount": amount}

    with open("expenses.csv", "a", encoding="utf-8", newline="") as csvfile:
        fieldnames = ['date', 'category', 'description', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(expense)

def sum_expenses(expenses):
    total = 0
    for expense in expenses:
        total += float(expense["amount"])
    return total

def print_expenses(expenses):
    for expense in expenses:
        print(expense["date"], expense["category"], expense["amount"])

def main():
    while True:
        try:
            print(textwrap.dedent(
            f"""\
            {"*" * 20}
            1. Show expenses
            2. Add expenses
            3. Sum expenses
            {"*" * 20}
            """))
            choice = input("What would you like to do? ")
            match choice:
                case "1":
                    print_expenses(load_expenses("expenses.csv"))
        except FileNotFoundError:
            print("No expenses found")

if __name__ == "__main__":
    main()