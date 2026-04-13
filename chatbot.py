
"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "COMP-1327 Faculty"
__version__ = "1.0.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

def get_account_number() -> int: 
    account_number = input("Please enter your account number:")

    try: 
        account_number = int(account_number)
    except:
        raise TypeError("Account number must be an int type")
    if account_number not in ACCOUNTS:
      raise ValueError("Account number entered does not exist.")
    return account_number   

def get_amount() -> float:
    get_amount = input("Enter an amount:")

    try:
        get_amount = float(get_amount)
    except:
        raise TypeError("Account must be a numeric type.")
    if get_amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    return get_amount   

def get_balance(get_account_number: int) -> str:
    if not isinstance (get_account_number, int):
        raise TypeError("Account number must be an int type.")
    
    if get_account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    
    balance = ACCOUNTS[get_account_number]
    return(f"Your current balance for account {get_account_number} is ${1000:,.2f}")

def make_deposit(account_number: int, amount: float) -> str:
    if not isinstance(account_number, int):
        raise TypeError("Account number must be an int type.")
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a numeric type.")
    if amount <= 0:
        raise ValueError("Amount must be a value greater than zero.")
    ACCOUNTS[account_number] = amount
    return(f"You have made a deposit of ${amount:,.2f} to account {account_number}.")

def get_task() -> str:
    task = input("what would you like to do (balance/deposit/exit)?:")
    if task not in VALID_TASKS:
        raise ValueError(f'"{task}" is an unknown task.')
    return task



if __name__ == "__main__":
    chatbot()
 
