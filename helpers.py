# # lib/helpers.py
# Importing the User, Account, and Transaction models
from models import User, Account, Transaction  

# Function to create a new user
def create_users():
    # Prompt user for name
    name = input("Enter your name: ") 
    # Create a new user with the entered name 
    user = User.create_user(username=name)  
    if user:
        # Confirm that the user was created
        print(f'User {name} created successfully!')  

# Function to create a new account for a specified user
def create_account():
    # Prompt user for user ID
    user_id = int(input("Enter user ID: "))
    # Create a new account for the user ID  
    account = Account.create_account(user_id=user_id) 
    if account:
        # Confirm that the account was created
        print(f'Account created successfully for user ID {user_id}.')  

# Function to deposit a specified amount into an account
def deposit(account_id, amount):
    # Retrieve the account by account ID
    account = Account.get_account_by_id(account_id) 
    if account:
        # Add the deposit amount to the account balance
        account.balance += amount  
        # Record the transaction
        Transaction.create_transaction(account_id=account.id, amount=amount) 
        # Confirm that the deposit was successful 
        print(f'Deposited {amount} to account ID {account_id}.')  

# Function to withdraw a specified amount from an account
def withdraw(account_id, amount):
    # Retrieve the account by account ID
    account = Account.get_account_by_id(account_id)  
    if account and account.balance >= amount:
        # Subtract the withdrawal amount from the account balance
        account.balance -= amount  
        # Record the transaction
        Transaction.create_transaction(account_id=account.id, amount=-amount) 
        # Confirm that the withdrawal was successful 
        print(f'Withdrew {amount} from account ID {account_id}.')  
    else:
        # Notify if the balance is insufficient
        print(f'Insufficient balance for account ID {account_id}.')  

# Function to view the balance of an account
def view_balance(account_id):
    # Retrieve the account by account ID
    account = Account.get_account_by_id(account_id)  
    if account:
        # Display the account balance for the specified account ID
        print(f'Balance for account ID {account_id}: {account.balance}')  
    else:
        # Notify if the account is not found
        print(f'Account ID {account_id} not found.')  

# Function to view all transactions for an account
def view_transactions(account_id):
    # Retrieve all transactions for the account
    transactions = Transaction.get_transactions_by_account_id(account_id)  
    if transactions:
        for transaction in transactions:
            # Display each transaction
            print(f'Transaction: {transaction.amount} on {transaction.transaction_date}')  
    else:
        # Notify if no transactions are found

        print(f'No transactions found for account ID {account_id}.')  
# Function to delete a user
def delete_user():
    # Prompt user for user ID to delete
    user_id = int(input("Enter user ID to delete: "))  
    # Delete the user with the specified ID
    User.delete_user(user_id)  
    # Confirm that the user was deleted
    print(f'User ID {user_id} deleted.')  

# Function to delete an account
def delete_account():
    # Prompt user for account ID to delete
    account_id = int(input("Enter account ID to delete: "))  
    # Delete the account with the specified ID
    Account.delete_account(account_id)  
    # Confirm that the account was deleted
    print(f'Account ID {account_id} deleted.')  

# Function to delete a transaction
def delete_transaction():
    # Prompt user for transaction ID to delete
    transaction_id = int(input("Enter transaction ID to delete: "))  
    # Delete the transaction with the specified ID
    Transaction.delete_transaction(transaction_id)  
     # Confirm that the transaction was deleted
    print(f'Transaction ID {transaction_id} deleted.') 
