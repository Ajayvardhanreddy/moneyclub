from models import Transactions, session


def add_transactions(txn_id, customer_id, txn_type, txn_amount, transaction_date):
    """

    This method helps to add transactions data to database

    """
    transactions_data = Transactions(txn_id=txn_id, customer_id=customer_id, txn_type=txn_type, txn_amount=txn_amount, transaction_date=transaction_date)
    session.add(transactions_data)
    session.commit()


transaction_id = int(input('Transaction Id: '))
cust_id = int(input('Customer Id: '))
transaction_type = input("Transaction Type: ")
transaction_amount = int(input("Amount: "))
txn_date = input("Transaction Date: ")

try:
    add_transactions(transaction_id, cust_id, transaction_type, transaction_amount, txn_date)
    print("Transaction Data added successfully!")
except:
    print("Error!!!")