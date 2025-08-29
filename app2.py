import os
from dotenv import load_dotenv
import gspread
from RemoteExpenseTracker import RemoteExpenseTracker
from CloudRepository import CloudRepository

def main():
    cloud_repo = CloudRepository()
    remote_expense_tracker = RemoteExpenseTracker(cloud_repo)
    # print(expense_tracker.expenses)
    # remote_expense_tracker.delete_expense(4)
    # remote_expense_tracker.display_expenses()

if __name__ == '__main__':
    main()