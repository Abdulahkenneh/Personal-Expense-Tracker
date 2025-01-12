import os
import pandas as pd

expensive =dict()
def get_user_expensive():
    '''
    the function get the user expesive
    :return: str of the expensive
    '''

    print('Enter your expensive ')

    date_of_expensive = input('Enter date in format: YYY-MM-DD ')
    cat_of_expensive =  input('Category of Expensive. Example Food or Travel ')
    amount           =  input('Enter the amount spent ')
    descripton       =  input('Please Enter a description: ')


    #initialize the variables
    expensive['date_of_expensive']=[]
    expensive['category_of_expensive']=[]
    expensive['amount']=[]
    expensive['Description']=[]

    #adding new expenisve
    expensive['date_of_expensive'].append(date_of_expensive)
    expensive['category_of_expensive'].append(cat_of_expensive)
    expensive['amount'].append(amount)
    expensive['Description'].append(descripton)
    print('Epensive has been Added successfully')

    return expensive

def view_expensive(expensive):
    if expensive is not None:

        print('\n These are your current expensive')
        for key, value in expensive.items():
            if not value or value==['']:
                print(f'No detail for {key}')
            else:
                print(f'{key} : {value}')
    else:
        print('The expensive is none')

def get_monthly_budget():
    budget = int(input('Please Enter Your monthly budget '))
    return budget

def calculate_total_expenive(budget,expensive):
    total_expensive = 0
    for amount in expensive['amount']:
        total_expensive +=int(amount)

    if budget > total_expensive:
        print('Warning your have exceed your monthly budget\n')
    elif total_expensive <0:
        print('Danger! you have a debpt')

    else:
        print(f'You have {total_expensive} left for the month\n')


def save_expensive_csv(expensive):
    df = pd.DataFrame(expensive)
    csv_file_path = 'expensive.csv'

    if not os.path.exists(csv_file_path):
        df.to_csv(csv_file_path, index=False)
    else:
        df.to_csv(csv_file_path, mode='a', header=False, index=False)

def read_csv():
    working_dir = os.getcwd()
    filename = 'expensive.csv'

    try:
        df = pd.read_csv(filename)

        if not df.empty:
            print("Here are your expenses:\n")
            print(df)
            expensive = handle_empty_csv()
            return expensive
        else:
            print("Your expenses file is empty.\n")
            handle_empty_csv()
    except pd.errors.EmptyDataError:
        print("You have not created any rows or columns for your expenses.\n")
        handle_empty_csv()


# Handle an empty CSV or initialize expenses
def handle_empty_csv():
    response = input("Do you wish to add new expenses? (yes/no): ").lower()
    if response.startswith('y'):
        expensive = get_user_expensive()
        save_expensive_csv(expensive)
        return expensive
    elif response.startswith('n'):
        print("No expenses added. Exiting.\n")
        exit()
    else:
        print("Invalid command. Please try again.\n")
        handle_empty_csv()


def main():
   expensive =read_csv()
   #expensive= get_user_expensive()
   view_expensive(expensive)
   budget=get_monthly_budget()
   calculate_total_expenive(budget, expensive)
   save_expensive_csv(expensive)
   handle_empty_csv()


if __name__ == "__main__":
    main()