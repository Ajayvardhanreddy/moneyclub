import psycopg2
from sqlalchemy import create_engine, ForeignKey, Sequence
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

db = create_engine('postgresql+psycopg2://postgres:ajayvardhan@localhost/moneycontrol')
base = declarative_base()


class Customer(base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    date_of_birth = Column(Date)
    transactions = relationship("Transactions", primaryjoin="and_(Customer.customer_id == Transactions.customer_id)")


class Transactions(base):
    __tablename__ = 'transactions'

    txn_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    txn_type = Column(String(10))
    txn_amount = Column(Integer)
    transaction_date = Column(Date)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)