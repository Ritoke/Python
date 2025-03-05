import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Initialize an empty Dataframe
columns = ['Date', 'Category', 'Description', 'Amount']
budget_df = pd.DataFrame(columns=columns)


#Functions needed for transaction
#Function to add transaction

def add_transaction(date, category, description, amount):
    global budget_df
    new_transaction = pd.DataFrame([[date, category, description, amount]], columns=columns)
    budget_df = pd.concat([budget_df, new_transaction], ignore_index=True)

#Function to view transaction
def view_transaction():
    global budget_df
    print(budget_df)


#function to save transaction to csv file
def save_transaction(file_path = 'budget_data.csv'):
    global budget_df
    budget_df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")


#Function to load transactions
def load_transaction(file_path = 'budget_data.csv'):
    global budget_df
    budget_df = pd.read_csv(file_path)
    print(f"Data loaded from {file_path}")


#User Input for transactions
def user():
    while True:
        print("\nBudget Traker Menu")
        print("1. Add Transaction")
        print("2. View Transaction")
        print("3. Save Transaction")
        print("4. Load Transaction")
        print("5. Analyze Data")
        print("6. Exit")
        choice = input("Enter your preferred choice (1-6)")

        if choice == '1':
            date = input('Enter the date of purchase (YYYY-MM-DD): ')
            category = input("Enter the Category (e.g., Income, Groceries, Rent): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            add_transaction(date, category, description, amount)
        elif choice == '2':
            view_transaction()
        elif choice == '3':
            file_path = input("Enter the file path to save transaction (default: budget_data.csv)")
            if file_path == '':
                file_path = 'budget_data.csv'
            save_transaction()
        elif choice == '4':
            file_path = input("Enter the file path to load transaction (default: budget_data.csv)")
            if file_path == '':
                file_path = 'budget_data.csv'
            load_transaction()
        elif choice == '5':
            analyze_data()
        elif choice == '6':
            print("Exiting Budget Tracker, Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def analyze_data():
    global budget_df

    #Total income
    total_income = budget_df[budget_df['Amount'] > 1000]['Amount'].sum()
    print(f"Total Income: ${total_income: .2f}")

    #total expenses
    total_expenses = budget_df[budget_df['Amount'] < 1000]['Amount'].sum()
    print(f"Total Expenses: ${total_expenses: .2f}")

    # Calculate the budget
    budget = total_income - total_expenses  #
    print(f"Budget (Total Income - Total Expenses): ${budget:.2f}")

    #Category-wise Breakdown
    category_breakdown = budget_df.groupby('Catogory')['Amount'].sum()

    print('passed first stage')

    #Plotting
    plt.figure(figure=(10, 6))
    category_breakdown.plot(kind='bar')
    plt.title('Category-wise Breakdown')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.show()

    #monthly trends (if date column exists)
    # if 'Date' in budget_df.columns:
    #     budget_df['Date'] = pd.to_date(budget_df['Date'])
    #     budget_df['Month'] = budget_df['Date'].dt.to_period('M')

    #     monthly_data = budget_df.groupby('Month').sum()['Amount']

    #     plt.figure(figsize = (14, 7))
    #     monthly_data.plot()
    #     plt.title('Monthly Expense Trend')
    #     plt.xlabel('Month')
    #     plt.ylabel('Amount')


user()



