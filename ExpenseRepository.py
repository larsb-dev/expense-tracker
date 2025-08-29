import os
from dotenv import load_dotenv
import gspread

def main():
    load_dotenv()
    cred_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
    sheet_id = os.getenv("SPREADSHEET_ID")
    if not cred_path:
        raise RuntimeError("Missing GOOGLE_SHEETS_CREDENTIALS")
    if not sheet_id:
        raise RuntimeError("Missing SPREADSHEET_ID")
    gc = gspread.service_account(filename=cred_path)
    sh = gc.open_by_key(sheet_id)
    sheet1 = sh.get_worksheet(0)
    print(sheet1.get("A1"))

if __name__ == "__main__":
    main()