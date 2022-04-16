from models import Transactions, Customer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime


def find_dob(dob):
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def calculate_savings(events):

    # Connect Data Base
    try:
        db = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(events['username'], events['password'], events['host'], events['database']))
    except:
        error = {
            "statusCode": 400,
            "message": "DataBase Connection Failed!"
        }
        return error

    Session = sessionmaker(db)
    session = Session()

    data = {}

    date = events['date']

    # filter transactions data based on date
    filt_transactions = session.query(Transactions).filter(Transactions.transaction_date == date)

    # list of ID's of customers on the given date
    customer_ids = set()
    for each_id in filt_transactions:
        if each_id.customer_id not in customer_ids:
            customer_ids.add(each_id.customer_id)

    if len(customer_ids) == 0:
        return "No transactions on the given date!"

    for each_id in list(customer_ids):
        filter_date_id_cols = session.query(Transactions).filter(Transactions.transaction_date == date, Transactions.customer_id == each_id)
        cust_filt = session.query(Customer).filter(Customer.customer_id == each_id)

        # age of each customer
        dob = cust_filt[0].date_of_birth

        age = find_dob(dob)

        # savings of each customer
        debit = 0
        credit = 0
        for each_txn in filter_date_id_cols:
            if (each_txn.txn_type).lower() == 'credit':
                credit += each_txn.txn_amount
            if (each_txn.txn_type).lower() == 'debit':
                debit += each_txn.txn_amount
        savings = credit-debit

        if age in data:
            savings = (savings + data[age])//2
        data[age] = savings

    result = {
        "statusCode": 200,
        "data": data
    }
    return result


events = {
    "database": "moneycontrol",
    "port": "8080",
    "host": "localhost",
    "username": "postgres",
    "password": "ajayvardhan",
    "date": "2022-04-16"
}

res = calculate_savings(events)
print(res)



