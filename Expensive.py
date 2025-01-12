import os
import pandas as pd

# Initialize global expense dictionary
expensive = {
    'date_of_expensive': [],
    'category_of_expensive': [],
    'amount': [],
    'Description': []
}

def get_user_expensive():
    """
    Get user expense details.
    :return: None
    """
    print('Enter your expense details:')
    date_of_expensive = input('Enter date (YYYY-MM-DD): ')
    cat_of_expensive = input('Category of Expense (e.g., Food, Travel): ')
    amount = input('Enter the amount spent: ')
    description = input('Please Enter a description: ')

    # Add new expense to global dictionary
    expensive['date_of_expensive'].append(date_of_expensive)
    expensive['category_of_expensive'].append(cat_of_expensive)
    expensive['amount'].append(amount)
    expensive['Description'].append(description)
    print('Expense has been added successfully.')


def view_expensive():
    """
    Display current expenses.
    :return: None
    """
    if expensive['date_of_expensive']:
        print('\nHere are your current expenses:')
        df = pd.DataFrame(expensive)
        print()
        print(df)
    else:
        print('No expenses recorded.')


def get_monthly_budget():
    """
    Get the user's monthly budget.
    :return: int
    """
    budget = int(input('Please enter your monthly budget: '))
    return budget


def calculate_total_expensive(budget):
    """
    Calculate and compare total expenses against the budget.
    :param budget: User's budget
    :return: None
    """
    total_expensive = sum(map(int, expensive['amount']))
    print(f'Total Expenses: {total_expensive}')

    if total_expensive > budget:
        print('Warning: You have exceeded your monthly budget!')
    else:
        print(f'You have {budget - total_expensive} left for the month.')


def save_expensive_csv():
    """
    Save expenses to a CSV file.
    :return: None
    """
    df = pd.DataFrame(expensive)
    csv_file_path = 'expenses.csv'

    # Check if file exists and handle headers
    if os.path.exists(csv_file_path):
        df.to_csv(csv_file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file_path, index=False)
    print('Expenses saved successfully.')
    view_expensive()


def read_csv():
    """
    Load expenses from CSV file.
    :return: None
    """
    csv_file_path = 'expenses.csv'

    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        if not df.empty:
            # Load data back into the global dictionary
            expensive.clear()
            for col in df.columns:
                expensive[col] = df[col].tolist()
            print('Expenses loaded from CSV.')
        else:
            print('CSV file is empty.')
    else:
        print('No CSV file found. Starting with empty expenses.')


def menu_options():
    """
    Display menu options to the user.
    :return: str
    """
    return input(
        """
        Choose an option:
        1: Add expenses
        2: View expenses
        3: Track budget
        4: Save expenses to CSV
        5: Exit
        Enter your choice: """
    )


def main():
    read_csv()
    while True:
        choice = menu_options()
        if choice == '1':
            get_user_expensive()
        elif choice == '2':
            view_expensive()
        elif choice == '3':
            budget = get_monthly_budget()
            calculate_total_expensive(budget)
        elif choice == '4':
            save_expensive_csv()
        elif choice == '5':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
