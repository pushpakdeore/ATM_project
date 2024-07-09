from db import execute_query, fetch_query

# User functions
def create_user(connection, username, password):
    query = """
    INSERT INTO Users (username, password) VALUES (%s, %s)
    """
    data = (username, password)
    execute_query(connection, query, data)

def authenticate_user(connection, username, password):
    query = "SELECT * FROM Users WHERE username = %s AND password = %s"
    data = (username, password)
    return fetch_query(connection, query, data)

# Account functions
def create_account(connection, user_id, account_number, account_type, balance=0.0):
    query = """
    INSERT INTO Accounts (user_id, account_number, balance, account_type) VALUES (%s, %s, %s, %s)
    """
    data = (user_id, account_number, balance, account_type)
    execute_query(connection, query, data)

def get_account(connection, account_number):
    query = "SELECT * FROM Accounts WHERE account_number = %s"
    data = (account_number,)
    return fetch_query(connection, query, data)

def update_balance(connection, account_number, amount):
    query = "UPDATE Accounts SET balance = balance + %s WHERE account_number = %s"
    data = (amount, account_number)
    execute_query(connection, query, data)

# Transaction functions
def create_transaction(connection, account_id, transaction_type, amount):
    query = """
    INSERT INTO Transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)
    """
    data = (account_id, transaction_type, amount)
    execute_query(connection, query, data)

# def get_transactions(connection, account_id):
#     query = "SELECT * FROM Transactions WHERE account_id = %s ORDER BY transaction_date DESC"
#     data = (account_id,)
#     return fetch_query(connection, query, data)
