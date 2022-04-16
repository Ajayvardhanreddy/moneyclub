from models import Customer, session


def add_customer(customer_id, first_name, last_name, date_of_birth):
    """

    This method helps to add customer data to database

    """
    customer_data = Customer(customer_id=customer_id, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
    session.add(customer_data)
    session.commit()


cust_id = int(input('Customer Id: '))
cust_first_name = input('First Name: ')
cust_last_name = input('Last Name: ')
cust_date_of_birth = input('Date of Birth: ')

try:
    add_customer(cust_id, cust_first_name, cust_last_name, cust_date_of_birth)
    print("Customer Data added successfully!")
except:
    print("Error!!!")