from Expense import Expense
from csv import DictReader, DictWriter
import datetime
from tabulate import tabulate
import os
from dotenv import load_dotenv
import gspread

class ExpenseTracker:

    def __init__(self, cloud_repo):
        self.expenses = []
        self.cloud_repo = cloud_repo

    # def load_expenses(self):
    #     worksheet = self.cloud_repo.get_worksheet()
    #     records = worksheet.get_all_records()
    #     for record in records:
    #         expense_obj = Expense(
    #             int(record["id"]),
    #             record["date"],
    #             record["category"],
    #             record["description"],
    #             float(record["amount"])
    #         )
    #         self.expenses.append(expense_obj)

    def save_expense(self, expense):
        worksheet = self.cloud_repo.get_worksheet()
        worksheet.append_row([
            expense.id,
            expense.date,
            expense.category,
            expense.description,
            expense.amount
        ])

    def add_expense(self):
        date = datetime.date.today().isoformat()
        category = input("What expense category do you wish to add? ")
        description = input("What expense do you wish to add? ")
        while True:
            try:
                amount = float(input("What amount do you wish to add? "))
                break
            except ValueError:
                print("Please enter a valid number for amount.")
        expense = Expense(self.get_previous_id() + 1, date, category, description, amount)
        self.save_expense(expense)

    def list_all_expenses(self):
        self.display_expenses(self.expenses)

    def list_expenses_by_category(self, category):
        if not category:
            self.display_expenses(self.expenses)
        else:
            filtered = [expense for expense in self.expenses if expense.category.lower() in category.lower()]
            self.display_expenses(filtered)

    def edit_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                expense.category = input("What expense category do you wish to edit? ")
                expense.description = input("What expense do you wish to edit? ")
                while True:
                    try:
                        expense.amount = float(input("What amount do you wish to add? "))
                        break
                    except ValueError:
                        print("Please enter a valid number for amount.")
        self.save_expense()

    def delete_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                self.expenses.remove(expense)
                self.save_expense()
                break

    def get_previous_id(self):
        worksheet = self.cloud_repo.get_worksheet()
        records = worksheet.get_all_records()
        if not records:
            return 0
        return max(int(record["id"]) for record in records)

    def display_expenses(self, expenses):
        if not expenses:
            print("No expenses to show.")
            return
        headers = ["id", "date", "category", "description", "amount"]
        rows = [[expense.id, expense.date, expense.category, expense.description, expense.amount] for expense in expenses]
        print(tabulate(rows, headers=headers, tablefmt="grid"))