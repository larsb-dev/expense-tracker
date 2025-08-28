from Expense import Expense
from csv import DictReader, DictWriter
import os
import datetime

class ExpenseTracker:
    FILEPATH = "expenses.csv"

    def __init__(self):
        self.expenses = []

    def load_expenses(self):
        with open(self.FILEPATH, "r", encoding="utf-8", newline="") as csvfile:
            reader = DictReader(csvfile, delimiter=',')
            for expense in reader:
                expense_obj = Expense(
                    int(expense["id"]),
                    expense["date"],
                    expense["category"],
                    expense["description"],
                    float(expense["amount"])
                )
                self.expenses.append(expense_obj)

    def save_expenses(self):
        file_exists = os.path.isfile(self.FILEPATH)
        fieldnames = ["id", "date", "category", "description", "amount"]
        with open(self.FILEPATH, "w", encoding="utf-8", newline="") as csvfile:
            writer = DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists or os.path.getsize(self.FILEPATH) == 0:
                writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense.__dict__)

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
        self.expenses.append(expense)
        self.save_expenses()

    def edit_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                expense.category = input("What expense category do you wish to edit? ")
                expense.description = input("What expense do you wish to edit? ")
                expense.amount = input("What amount do you wish to edit? ")
                break
        self.save_expenses()

    def delete_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                self.expenses.remove(expense)
                self.save_expenses()
                break

    def get_previous_id(self):
        return int(self.expenses[-1].id) if self.expenses else 0

    def get_expense_by_id(self, id):
        for expense in self.expenses:
            if expense.id == id:
                return expense
        raise Exception("Expense not found")

