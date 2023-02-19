import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)


def get_sales_row():
    """
    Get sales figures from the user
    """
    while True:
        print("Please enter sales dta from the last market.")
        print("Should be 6 comma delimited numbers - 10,20,30,40,50,60\n")
        data_str = input("Enter your data here: ")
        sales_row = data_str.split(",")
        if validate_data(sales_row):
            break
    sales_row = [int(num) for num in sales_row]
    return sales_row


def validate_data(data):
    """
    checks for 6 element array of numbers
    """
    print(data)
    try:
        [int(num) for num in data]
        if len(data) != 6:
            raise ValueError(
                f"6 values required - you gave {len(data)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False
    return True


def update_sales_worksheet(sales_row):
    """
    update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(sales_row)
    print("Update success\n")

def update_surplus_worksheet(surplus_row):
    """
    update surplus worksheet, add new row with the list data provided
    """
    print("Updating surplus worksheet")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(surplus_row)
    print("Update success\n")


def calculate_surplus_row(sales_row):
    """
    comapere sales with stockand calculate surplus for each type

    surplus = stock - sales
    posiive result = waste
    negative result = extra made when stock was exhausted
    """
    print("Caloculating surplus data...")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    # stock_row = [int(num) for num in stock_row]
    surplus_row = []
    for stock, sales in zip(stock_row, sales_row):
        surplus_row.append(int(stock) - sales)

    return surplus_row


def main():
    """
    main program flow
    """
    sales_row = get_sales_row()
    update_sales_worksheet(sales_row)
    # surplus_row = calculate_surplus_row(sales_row)
    update_surplus_worksheet(calculate_surplus_row(sales_row))


main()
