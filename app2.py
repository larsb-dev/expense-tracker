import os
from dotenv import load_dotenv
import gspread
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from RemoteExpenseTracker import RemoteExpenseTracker
from CloudRepository import CloudRepository

def main():
    try:
        cloud_repo = CloudRepository()
        cloud_repo.connect()
    except RefreshError as e:
        print(e)
    # print(cloud_repo.get_worksheet(2))
    # print(expense_tracker.expenses)
    # remote_expense_tracker.delete_expense(4)
    # remote_expense_tracker.display_expenses()

if __name__ == '__main__':
    main()