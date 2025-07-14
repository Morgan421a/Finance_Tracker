class Expense:
    def __init__(self, merchant, amount, category, description, date):
        self.merchant = merchant
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

def new_expense():
    merchant = input("Merchant: "),
    amount = float(input("Amount: "))
    category = input("Category - Essential, Food, Groceries, Recurring, Luxury, Savings, Misc (E, F, G, R, L, S, M): ").lower()
    description = input("Description: ")
    date = input("Date: ")

    expense = Expense(
        merchant = merchant,
        amount = amount,
        category = category,
        description = description,
        date = date
    )
    return expense
Expenses = []

power = True

while power:
   
    new_expense()



