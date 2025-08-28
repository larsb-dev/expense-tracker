from ExpenseTracker import ExpenseTracker

def main():
    expense_tracker = ExpenseTracker("expenses.csv")
    try:
        expense_tracker.load_expenses()
        expense_tracker.add_expense()
        print(expense_tracker.expenses)
        # expense_tracker.delete_expense(1)
    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    main()