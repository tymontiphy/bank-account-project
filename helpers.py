# lib/helpers.py


from models import User, Account, Transaction


def create_users():
    name = input("Enter your name: ")
    user = User.create_user(username=name)
    if user:
        print(f'User {name} created successfully!')

def create_account():
    user_id = int(input("Enter user ID: "))
    account = Account.create_account(user_id=user_id)
    if account:
        print(f'Account created successfully for user ID {user_id}.')

def deposit(account_id, amount):
    account = Account.get_account_by_id(account_id)
    if account:
        account.balance += amount
        Transaction.create_transaction(account_id=account.id, amount=amount)
        print(f'Deposited {amount} to account ID {account_id}.')

def withdraw(account_id, amount):
    account = Account.get_account_by_id(account_id)
    if account and account.balance >= amount:
        account.balance -= amount
        Transaction.create_transaction(account_id=account.id, amount=-amount)
        print(f'Withdrew {amount} from account ID {account_id}.')
    else:
        print(f'Insufficient balance for account ID {account_id}.')

def view_balance(account_id):
    account = Account.get_account_by_id(account_id)
    if account:
        print(f'Balance for account ID {account_id}: {account.balance}')
    else:
        print(f'Account ID {account_id} not found.')

def view_transactions(account_id):
    transactions = Transaction.get_transactions_by_account_id(account_id)
    if transactions:
        for transaction in transactions:
            print(f'Transaction: {transaction.amount} on {transaction.transaction_date}')
    else:
        print(f'No transactions found for account ID {account_id}.')

def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    User.delete_user(user_id)
    print(f'User ID {user_id} deleted.')

def delete_account():
    account_id = int(input("Enter account ID to delete: "))
    Account.delete_account(account_id)
    print(f'Account ID {account_id} deleted.')

def delete_transaction():
    transaction_id = int(input("Enter transaction ID to delete: "))
    Transaction.delete_transaction(transaction_id)
    print(f'Transaction ID {transaction_id} deleted.')
