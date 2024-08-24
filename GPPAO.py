# 13/08/2024 : Simple budgeting app made by thedeadbolt
# update fragmentar noutros ficheiros (a fazer)
# update2 - add mais budget (a fazer)

def add_expense(expenses, description, amount, expense_type, budget):
    expenses.append({"description": description, "amount": amount, "type": expense_type})
    print(f"Added {expense_type} expense: {description}, Amount: {amount}")

    if get_total_expenses(expenses) > budget:
        print("Warning: You have exceeded your budget!")

def get_total_expenses(expenses, expense_type=None):
    total = 0
    for expense in expenses:
        if expense_type is None or expense["type"] == expense_type:
            total += expense["amount"]
    return total

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print("Key Expenses:")
    for expense in expenses:
        if expense["type"] == "key":
            print(f"- {expense['description']}: {expense['amount']}")

    print("Luxury Expenses:")
    for expense in expenses:
        if expense["type"] == "luxury":
            print(f"- {expense['description']}: {expense['amount']}")

    key_total = get_total_expenses(expenses, "key")
    luxury_total = get_total_expenses(expenses, "luxury")

    print(f"Total Key Expenses: {key_total}")
    print(f"Total Luxury Expenses: {luxury_total}")
    print(f"Total Spent: {key_total + luxury_total}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")

    if get_total_expenses(expenses) > budget:
        print("Warning: You have exceeded your budget!")

def main():
    print("Welcome to thedeadbolt's monthly budgeting app (TMBA)!")
    initial_budget = float(input("Please insert your budget for this month: "))
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add your expenses for this month")
        print("2. Show budget details")
        print("3. Exit TMBA")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter your expense description: ")
            amount = float(input("Enter your expense amount: "))
            expense_type = input("Is this a 'key' expense or a 'luxury' expense? ").lower()

            while expense_type not in ["key", "luxury"]:
                print("Invalid choice. Please enter 'key' or 'luxury'.")
                expense_type = input("Is this a 'key' expense or a 'luxury' expense? ").lower()

            add_expense(expenses, description, amount, expense_type, budget)

        elif choice == "2":
            show_budget_details(budget, expenses)

        elif choice == "3":
            print("Exiting TMBA, see you soon!")
            break

        else:
            print("Invalid choice, please input a valid choice.")

if __name__ == "__main__":
    main()





