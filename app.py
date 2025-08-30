from ExpenseTracker import ExpenseTracker
from CloudRepository import CloudRepository
import textwrap

def input_number(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")

def main():
    try:
        cloud_repo = CloudRepository()
        expense_tracker = ExpenseTracker(cloud_repo)
        cloud_repo.authenticate()
        cloud_repo.load_sheets()
    except ValueError as e:
        print(f"Failed to initialize cloud repository: {e}")
        return

    end = False
    while not end:
        try:
            print(textwrap.dedent(
                f"""
            Options to chose from:
            1. Add an expense
            2. List all expenses
            3. Edit an expense
            4. Delete an expense
            5. Exit the app
            """))
            choice = input("What would you like to do? ")
            match choice:
                case "1":
                    expense_tracker.add_expense()
                case "2":
                    print("")
                    expense_tracker.list_all_expenses()
                case "3":
                    id = input_number("What expense do you wish to edit? ")
                    expense_tracker.edit_expense(id)
                case "4":
                    id = input_number("What expense do you wish to delete? ")
                    expense_tracker.delete_expense(id)
                case "5":
                    end = True
        except Exception as e:
            print(f"Something went wrong {e}")

if __name__ == '__main__':
    main()