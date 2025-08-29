import os
from dotenv import load_dotenv
import gspread

class CloudRepository:

    def __init__(self):
        load_dotenv()
        self.cred_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
        self.sheet_id = os.getenv("SPREADSHEET_ID")
        if not self.cred_path:
            raise RuntimeError("Missing GOOGLE_SHEETS_CREDENTIALS")
        if not self.sheet_id:
            raise RuntimeError("Missing SPREADSHEET_ID")
        self.client = gspread.service_account(filename=self.cred_path)
        self.spreadsheet = self.client.open_by_key(self.sheet_id)
        self.worksheet = self.spreadsheet.get_worksheet(0)

    def get_spreadsheet(self):
        return self.spreadsheet

    def get_worksheet(self):
        return self.worksheet

    def set_worksheet(self, id):
        self.worksheet = self.spreadsheet.get_worksheet(id)