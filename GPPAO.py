# 24/08/2024: GPPAOv2
# addded saving expenses into a json file

import json

def save_data(budget, expenses, filename="budget_data.json"):  # defining the save data into a json file function
    data = {'budget': budget, "expenses": expenses}
    with open(filename, "w") as file:  # write as file
        json.dump(data, file)  # function within json that dumps it into the json file
    print("Budget and expenses saved successfully!")

def load_data(filename="budget_data.json"):  # defining loading the data of the saved json file
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        print("Budget and expenses loaded successfully!")
        return data["budget"], data["expenses"]
    except FileNotFoundError:
        print("No previous expense planning was found. Starting with a new budget.")
        return None, []


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
    print("Welcome to the General Personal Planning and Allocation of Obligations App (GPPAO)!")
    budget, expenses = load_data()  # load previous data if available

    if budget is None:
        initial_budget = float(input("Please insert your budget for this month: "))
        budget = initial_budget

    while True:
        print("\nWhat would you like to do?")
        print("1. Add your expenses for this month")
        print("2. Show budget details")
        print("3. Save your monthly expenses and Exit GPPAO")
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
            save_data(budget, expenses)
            print("Exiting GPPAO, see you soon!")
            break

        else:
            print("Invalid choice, please input a valid choice.")


if __name__ == "__main__":
    main()
