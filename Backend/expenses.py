class Expense:
    def __init__(self, merchant, amount, category, description, date):
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __repr__(self):
        return (f"Merchant: {self.merchant},Amount: {self.amount}, "
                f"Category: {self.category}, Description: {self.description}, Date: {self.date}")

def new_expense():
    category_check = True
    merchant = input("Merchant: ").title(),
    amount = float(input("Amount: "))
    while category_check == True:
        category = input("Category - Essential, Food, Groceries, Recurring, Luxury, Savings, Misc (E, F, G, R, L, S, M): ").lower()
        if category == "e":
            category = "Essential"
            category_check = False
        elif category == "f":
            category = "Food"
            category_check = False
        elif category == "g":
            category = "Groceries"
            category_check = False
        elif category == "r":
            category = "Recurring"
            category_check = False
        elif category == "l":
            category = "Luxury"
            category_check = False
        elif category == "s":
            category = "Savings"
            category_check = False
        elif category == "m":
            category = "Misc"
            category_check = False
        else:
            print("Invalid Input, Please Try Again")
    
    description = input("Description: ").title()
    date = input("Date: ")

    expense = Expense(
        merchant = merchant,
        amount = amount,
        category = category,
        description = description,
        date = date
    )
    return expense
Expenses = {}

power = True

while power:
   
    expense = new_expense()

    expense_name = input("Name of Expense: ").title()

    Expenses[expense_name] = expense

    print(Expenses)

    next_expense = True
    while next_expense:
        n_expense = input("Continue/Shutdown (C / S): ").lower()

        if n_expense == "s":
            print("Shutting Down...")
            next_expense = False
            power = False
        elif n_expense == "c":
            next_expense = False
        elif n_expense != "c" and n_expense != "s":
            print("Invalid Input, Please try again.")





