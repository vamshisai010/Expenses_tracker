# Expenses_tracker

# Documentation:


  # INTRODUCTION:
    The Expense Tracker is a Python program designed to help users manage their expenses efficiently. It provides functionalities for recording expenses, viewing monthly expense summaries, category-wise expense 
    summaries, and more.

  # INSTALLATION:
    Download the above code and run it using python interpreter or visual studio code.

  # PROGRAM STRUCTURE:
    The Expense Tracker program consists of the following components:
    
  # ExpenseTracker Class:
    The ExpenseTracker class is the core of the program, responsible for managing expenses.
    It has methods to add expenses, save expenses to a file, load expenses from a file, calculate monthly expense summaries, and calculate category-wise expense summaries.
    
  # Expense Data:
    Each expense is represented as a dictionary containing keys for date, amount, description, and category.
    
  # User Input Functions:
    get_user_input(): Prompts the user to input details of a new expense.
    
  # Main Functionality:
    main(): Main function to run the expense tracker program.
    Presents a menu of options for users to interact with the program.
    
  # Menu Options:
    Add an Expense: Allows the user to input details of a new expense and adds it to the list of expenses.
    View Monthly Expense Summary: Prompts the user to enter a month and year, then calculates and displays the total expenses for that month and year.
    View Category-wise Expense Summary: Calculates and displays the total expenses for each category.
    Show Expenses Data: Displays all recorded expenses with their details (date, amount, description, category).
    Exit: Saves the expenses to a file and exits the program.

  # Error Handling:
    The program handles errors such as invalid user inputs or missing expense data file.
    
  # File Handling:
    The program saves expenses to a JSON file (expenses.json) and loads expenses from it when the program starts.

  # CONCLUSION:
    The Expense Tracker program offers a user-friendly interface for managing expenses effectively. With its intuitive functionalities and clear documentation, users can easily track their expenses and make           informed financial decisions.





