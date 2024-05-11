import json
from datetime import datetime
print("=========================EXPENSES TRACKER=========================")
class ExpenseTracker:
    def __init__(self):
        self.expenses = []  #Initializing an empty list to store expenses

    def add_expense(self, amount, description, category, date):
        #Add a new expense to the expenses list
        self.expenses.append({
            'date': date,  #adding date
            'amount': amount,  #adding amount
            'description': description,  #adding description
            'category': category  #adding category
        })

    def save_expenses(self, filename='expenses.json'):  #expenses saved as filename expenses.json
        with open(filename, 'w') as file:  #file will open and add and write the expenses
            json.dump(self.expenses, file)

    def load_expenses(self, filename='expenses.json'):
        try:
            #Load the expenses from a JSON file
            with open(filename, 'r') as file:
                self.expenses = json.load(file)  #shows the expenses by reading it if data found
        except FileNotFoundError:
            print("No expense data found.")  #Handle case where no expense data file is found

    def get_monthly_summary(self, month, year):
        total_expenses = 0  #Iterate through expenses and calculate total expenses for the given month and year
        for expense in self.expenses:
            #Split the date string into year, month, and day
            expense_year, expense_month, _ = expense['date'].split('-')
            #Check if the expense date matches the given month and year
            if expense_month == month and expense_year == year:
                total_expenses += expense['amount']
        return total_expenses

    def get_category_summary(self):
        category_summary = {} #Iterate through expenses and calculate total expenses for each category
        for expense in self.expenses:
            category = expense['category']  #Update the total expenses for the category
            if category in category_summary:
                category_summary[category] += expense['amount']
            else:
                category_summary[category] = expense['amount']
        return category_summary

#function to get user input for adding expense
def get_user_input():
    #get user input for amount, description, category, and date
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., Groceries, Housing, Food Items, Education, Savings, Debts, Transportation, Entertainment): ")
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    return amount, description, category, date

def main():
    tracker = ExpenseTracker()  #assigning expensetracker funtion to tracker
    tracker.load_expenses()  #calling load_epenses and load the data
    #Choose the inputs
    while True:
        print("\nMenu:")
        print("1. Add an expense")
        print("2. View monthly expense summary")
        print("3. View category-wise expense summary")
        print("4. Show expenses data")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            amount, description, category, date = get_user_input()
            tracker.add_expense(amount, description, category, date) #calling add_expense funtion
        elif choice == '2':
            month = input("Enter the month (MM): ")
            year = input("Enter the year (YYYY): ")
            monthly_summary = tracker.get_monthly_summary(month, year)  #calling get_monthly_summary funtion
            print(f"\nTotal expenses for {month}-{year}: ${monthly_summary}")
        elif choice == '3':
            category_summary = tracker.get_category_summary()  #calling get_category_summary funtion
            print("\nCategory-wise expenses summary:")
            for category, amount in category_summary.items():
                print(f"{category}: ${amount}")
        elif choice == '4':
            print("\nExpenses data:")
            if tracker.expenses:  #calling expense funtion to show the data
                for idx, expense in enumerate(tracker.expenses, start=1):
                    print(f"{idx}. Date: {expense['date']}, Amount: ${expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")
            else:
                print("No expenses recorded.")
        elif choice == '5':
            tracker.save_expenses() #calling save_expenses funtion and save the data and exit the program
            print("Exiting the expense tracker. Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":  #calling main funtion 
    main()
