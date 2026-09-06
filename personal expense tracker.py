# Personal Expense Tracker

expenses = []

def add_expense():
    amount = float(input("Enter Amount: "))
    category = input("Enter Category (Food/Travel/Shopping/Education): ")

    expense = {
        "Amount": amount,
        "Category": category
    }

    expenses.append(expense)

    file = open("expenses.txt", "a")
    file.write(f"{amount} - {category}\n")
    file.close()

    print("Expense Added Successfully!\n")


def view_expenses():
    if len(expenses) == 0:
        print("No Expenses Found!\n")
    else:
        print("\n----- Expense List -----")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Amount: ₹{expense['Amount']} | Category: {expense['Category']}")
        print()

        
def total_expense():
    total = 0

    for expense in expenses:
        total += expense["Amount"]

    print(f"\nTotal Expense = ₹{total}\n")


while True:
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You For Using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Please Try Again.\n")
