from csv import DictReader, DictWriter
import csv
import datetime
import os
import textwrap

from tabulate import tabulate








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
    # end = False
    # while not end:
    #     try:
    #         print(textwrap.dedent(
    #         f"""\
    #         {"*" * 33}
    #         Welcome to the Expense Tracker 🤑\n
    #         Options to chose from:
    #         1. Add an expense
    #         2. List all expenses
    #         3. List all expenses by category
    #         4. Edit an expense
    #         5. Delete an expense
    #         6. Exit the app
    #         {"*" * 33}
    #         """))
    #         choice = input("What would you like to do? ")
    #         match choice:
    #             case "1":
    #                 print_expenses(load_expenses("expenses.csv"))
    #             case "2":
    #                 add_expense()
    #             case "3":
    #                 summary = sum_expenses(load_expenses("expenses.csv"))
    #                 print(summary)
    #             case "4":
    #                 end = True
    #     except FileNotFoundError:
    #         print("No expenses found")
        expenses = load_expenses()
        add_expense(expenses)

if __name__ == "__main__":
    main()