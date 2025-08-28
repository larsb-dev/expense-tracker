from Expense import Expense
from csv import DictReader, DictWriter
import datetime
from tabulate import tabulate

class ExpenseTracker:

    def __init__(self, filepath):
        self.filepath = filepath
        self.expenses = []

    def load_expenses(self):
        with open(self.filepath, "r", encoding="utf-8", newline="") as csvfile:
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
        fieldnames = ["id", "date", "category", "description", "amount"]
        with open(self.filepath, "w", encoding="utf-8", newline="") as csvfile:
            writer = DictWriter(csvfile, fieldnames=fieldnames)
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
                print("\nPlease enter a valid number for amount.")
        expense = Expense(self.get_previous_id() + 1, date, category, description, amount)
        self.expenses.append(expense)
        self.save_expenses()

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
        self.save_expenses()

    def delete_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                self.expenses.remove(expense)
                self.save_expenses()
                break

    def get_previous_id(self):
        return int(self.expenses[-1].id) if self.expenses else 0

    def display_expenses(self, expenses):
        if not expenses:
            print("No expenses to show.")
            return
        headers = ["id", "date", "category", "description", "amount"]
        rows = [[expense.id, expense.date, expense.category, expense.description, expense.amount] for expense in expenses]
        print(tabulate(rows, headers=headers, tablefmt="grid"))