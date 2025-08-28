from ExpenseTracker import ExpenseTracker
import textwrap

def input_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def main():

    expense_tracker = ExpenseTracker("expenses.csv")
    expense_tracker.load_expenses()

    end = False
    while not end:
        try:
            print(textwrap.dedent(
            f"""
            Options to chose from:
            1. Add an expense
            2. List all expenses
            3. List all expenses by category
            4. Edit an expense
            5. Delete an expense
            6. Exit the app
            """))
            choice = input("What would you like to do? ")
            match choice:
                case "1":
                    expense_tracker.add_expense()
                case "2":
                    print("")
                    expense_tracker.list_all_expenses()
                case "3":
                    category = input("What category would you like to see? ")
                    print("")
                    expense_tracker.list_expenses_by_category(category)
                case "4":
                    id = input_number("What expense do you wish to edit? ")
                    expense_tracker.edit_expense(id)
                case "5":
                    id = input_number("What expense do you wish to delete? ")
                    expense_tracker.delete_expense(id)
                case "6":
                    end = True
        except FileNotFoundError:
            print("Expenses file not found")

if __name__ == '__main__':
    main()