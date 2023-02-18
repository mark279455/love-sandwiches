import gspread
from google.oauth2.service_account import Credentials

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




def get_sales_data():
    """
    Get sales figures from the user
    """
    print("Please enter sales dta from the last market.")
    print("Should be 6 comma delimited numbers - 10,20,30,40,50,60\n")
    data_str = input("Enter your data here: ")
    sales_data = data_str.split(",")
    validate_data(sales_data)




def validate_data(data):
    """
    checks for 6 element array of numbers
    """
    print(data)
    try:
        if len(data) != 6:
            raise ValueError(
                f"6 values required - you gave {len(data)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")

get_sales_data()