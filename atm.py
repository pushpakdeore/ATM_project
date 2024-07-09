from db import create_connection
from model import create_user, authenticate_user, create_account, get_account, update_balance, create_transaction #get_transactions

def register(connection):
    username = input("Enter username: ")
    password = input("Enter password: ")
    create_user(connection, username, password)
    print("User registered successfully")

def authenticate(connection):
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = authenticate_user(connection, username, password)
    if user: 
        print("Authentication successful")
        return user[0]
    else:
        print("Authentication failed")
        return None

def create_account_for_user(connection, user):
    account_number = input("Enter account number: ")
    account_type = input("Enter account type: ")
    create_account(connection, user['user_id'], account_number, account_type)
    print("Account created successfully")

def deposit(connection):
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    account = get_account(connection, account_number)
    if account:
        update_balance(connection, account_number, amount)
        create_transaction(connection, account[0]['account_id'], "deposit", amount)
        print("Deposit successful")
    else:                            
        print("Account not found")

def withdraw(connection):
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    account = get_account(connection, account_number)
    if account:
        if account[0]['balance'] >= amount:
            update_balance(connection, account_number, -amount)
            create_transaction(connection, account[0]['account_id'], "withdrawal", amount)
            print("Withdrawal successful")
        else:
            print("Insufficient funds")
    else:
        print("Account not found")

def main():
    connection = create_connection()

    while True:
        print("\n1. Register")
        print("2. Authenticate")
       # print("3. Create Account")
        # print("4. Deposit")
        # print("5. Withdraw")
        # print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register(connection)
        elif choice == "2":
            user = authenticate(connection)
            if user:
                while True:
                    print("\n1. Create Account")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    sub_choice = input("Enter choice: ")
                    if sub_choice == "1":
                        create_account_for_user(connection, user)
                    elif sub_choice == "2":
                        deposit(connection)
                    elif sub_choice == "3":
                        withdraw(connection)
                    elif sub_choice == "4":
                        break
                    else:
                        print("Invalid choice")
        # elif choice == "3":
        #     print("Authenticate first to create an account")
        # elif choice == "4":
        #     print("Authenticate first to deposit")
        # elif choice == "5":
        #     print("Authenticate first to withdraw")
        # elif choice == "6":
        #     break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
