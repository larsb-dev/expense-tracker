from Expense import Expense
from csv import DictReader, DictWriter
import datetime

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
        amount = self.get_amount_input("What amount do you wish to add? ")
        expense = Expense(self.get_previous_id() + 1, date, category, description, amount)
        self.expenses.append(expense)
        self.save_expenses()

    def list_all_expenses(self):
        print_expenses(self.expenses)

    def list_expenses_by_category(self, category):
        if not category:
            print_expenses()
        else:
            filtered = [expense for expense in expenses if expense.category.lower() in category.lower()]
            print_expenses(filtered)

    def edit_expense(self, id):
        for expense in self.expenses:
            if expense.id == id:
                expense.category = input("What expense category do you wish to edit? ")
                expense.description = input("What expense do you wish to edit? ")
                expense.amount = self.get_amount_input("What amount do you wish to add? ")
                break
        self.save_expenses()

    def get_amount_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number for amount.")

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

    def print_expenses(self, expenses):
        if not expenses:
            print("No expenses to show.")
            return
        headers = ["date", "category", "description", "amount"]
        rows = [[expense.date, expense.category, expense.description, expense.amount] for expense in expenses]
        print(tabulate(rows, headers=headers, tablefmt="grid"))