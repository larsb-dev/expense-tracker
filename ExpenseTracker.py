from Expense import Expense
import datetime
from tabulate import tabulate

class ExpenseTracker:

    def __init__(self, cloud_repo):
        self.cloud_repo = cloud_repo

    def save_expense(self, expense):
        worksheet = self.cloud_repo.get_worksheet(0)
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
        worksheet = self.cloud_repo.get_worksheet(0)
        records = worksheet.get_all_records()
        if not records:
            print("No expenses to show.")
            return
        headers = ["id", "date", "category", "description", "amount"]
        rows = [[expense["id"], expense["date"], expense["category"], expense["description"], expense["amount"]] for expense in records]
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def edit_expense(self, id):
        worksheet = self.cloud_repo.get_worksheet(0)
        records = worksheet.get_all_records()
        for idx, record in enumerate(records, start=2):
            if record["id"] == id:
                category = input("What expense category do you wish to edit? ")
                description = input("What expense do you wish to edit? ")
                while True:
                    try:
                        amount = float(input("What amount do you wish to add? "))
                        break
                    except ValueError:
                        print("Please enter a valid number for amount.")
                worksheet.update([[category, description, amount]], f'C{idx}:E{idx}')
                break
        print(f"An expense with id {id} was not found.")

    def delete_expense(self, id):
        worksheet = self.cloud_repo.get_worksheet(0)
        records = worksheet.get_all_records()
        for idx, expense in enumerate(records, start=2):
            if id == expense["id"]:
                worksheet.delete_rows(idx)
                break
        print(f"An expense with id {id} was not found.")

    def get_previous_id(self):
        worksheet = self.cloud_repo.get_worksheet(0)
        records = worksheet.get_all_records()
        if not records:
            return 0
        return max(int(record["id"]) for record in records)