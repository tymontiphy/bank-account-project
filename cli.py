from helpers import (
    create_users, create_account, deposit, withdraw, view_balance, view_transactions,
    delete_user, delete_account, delete_transaction
)

def main():
    # Welcome message
    print("Welcome to the Bank Account Management System!")

    while True:
        # Display the menu options to the user
        print("\nMenu:")
        print("1. Create User")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View Balance")
        print("6. View Transactions")
        print("7. Delete User")
        print("8. Delete Account")
        print("9. Delete Transaction")
        print("10. Exit")

        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")

        # Execute the corresponding function based on user input
        if choice == '1':
            create_users()  
        elif choice == '2':
            create_account() 
        elif choice == '3':
            account_id = int(input("Enter account ID: "))  
            amount = float(input("Enter amount to deposit: "))  
            deposit(account_id, amount)
        elif choice == '4':
            account_id = int(input("Enter account ID: ")) 
            amount = float(input("Enter amount to withdraw: "))  
            withdraw(account_id, amount) 
        elif choice == '5':
            account_id = int(input("Enter account ID: "))  
            view_balance(account_id)
        elif choice == '6':
            account_id = int(input("Enter account ID: ")) 
            view_transactions(account_id)  
        elif choice == '7':
            delete_user()
        elif choice == '8':
            delete_account() 
        elif choice == '9':
            delete_transaction()  
        elif choice == '10':
            print("Goodbye!")  # Exit message
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu option

# Ensure the main function is called when the script is executed
if __name__ == '__main__':
    main()




