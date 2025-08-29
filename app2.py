import os
from dotenv import load_dotenv
import gspread
from ExpenseTracker import ExpenseTracker
from CloudRepository import CloudRepository

def main():
    # load_dotenv()
    # cred_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
    # sheet_id = os.getenv("SPREADSHEET_ID")
    # gc = gspread.service_account(filename=cred_path)
    # print(gc.open_by_key(sheet_id))

    cloud_repo = CloudRepository()

    expense_tracker = ExpenseTracker(cloud_repo)
    expense_tracker.add_expense()
    print(expense_tracker.expenses)

if __name__ == '__main__':
    main()