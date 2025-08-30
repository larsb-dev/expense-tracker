import os
from dotenv import load_dotenv
import gspread
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from gspread import WorksheetNotFound, SpreadsheetNotFound
from gspread.exceptions import APIError

class CloudRepository:

    def __init__(self):
        load_dotenv()
        self.credentials = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
        self.sheet_id = os.getenv("SPREADSHEET_ID")
        self.client = None
        self.spreadsheet = None
        self.worksheets = []

    def authenticate(self):
        try:
            self.client = gspread.service_account(filename=self.credentials)
        except RefreshError:
            raise RefreshError("Can't connect to Google Sheets API due to wrong credentials")

    def load_sheets(self):
        try:
            self.spreadsheet = self.client.open_by_key(self.sheet_id)
            self.worksheets = self.spreadsheet.worksheets()
        except SpreadsheetNotFound:
            raise SpreadsheetNotFound(f"Spreadsheet with the id {self.sheet_id} not found")

    def get_worksheet(self, id):
        for worksheet in self.worksheets:
            if id == self.worksheets.index(worksheet):
                return self.worksheets[id]
        raise WorksheetNotFound("Worksheet not found.")