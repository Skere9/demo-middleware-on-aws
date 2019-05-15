#
# File: middleware.py
#

import json 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import request 
from flask import jsonify
from flask.views import View

from services.data_provider_service import DbConnectService
from services.data_provider_service import session_scope 
from models.model import Model 
from models.customer import Customer 

# API for CUSTOMER

def transformQueryOutputToJson(pParameter):
    '''Transform queried data (pParameter)
    to jsonified output for sending via a REST interface.
    '''
    # Serialize the instances
    interimResult = [the_parm.serialize() for the_parm in pParameter]
    # Jsonify the list 
    return jsonify(interimResult)

def get_customer(pCustomerId, serialize=True):
    # This is the API to return a single customer with an ID of pCustomerId
    with session_scope() as s:
        the_customers = []
        the_customers = s.query(Customer).filter(Customer.id == pCustomerId).all()
        if serialize:
            return transformQueryOutputToJson(the_customers)
        else:
            return the_customers   

def get_customers(serialize=True):
    # This is the API to return all customers
    with session_scope() as s:
        the_customers = s.query(Customer).order_by(Customer.id).all()
        if serialize:
            return transformQueryOutputToJson(the_customers)
        else:
            return jsonify(the_customers)   

def add_customer(pCustomer):
    theResponse = 'This is the API to add a new customer'
    with session_scope() as s: 
        the_result = s.add(pCustomer)
        return the_result

def mod_customer(pCustomer, serialize=True):
    theResponse = 'This is the API to update an existing customer'
    with session_scope() as s:
        print('The customer info is: ')
        print(pCustomer.id)
        print(pCustomer.firstName)
        print(pCustomer.lastName)
        print(pCustomer.category)
        print('That was it!')
        items_updated= s.query(Customer).filter(Customer.id == pCustomer.id).update({
            Customer.firstName: pCustomer.firstName,
            Customer.lastName: pCustomer.lastName,
            Customer.category: pCustomer.category
            }, synchronize_session=False)
        if items_updated > 0:
            return jsonify({"data": items_updated})
        else:
            return jsonify({"data": 0})  

def rem_customer(pCustomerId, serialize=True):
    theResponse = 'This is the API to remove a single customer'
    print('The ID to delete is:')
    print(pCustomerId)
    print('So let us see if that works.')
    with session_scope() as s:
        items_deleted = s.query(Customer).filter(Customer.id == pCustomerId).delete()
        if items_deleted > 0:
            return jsonify({"data": items_deleted})
        else:
            return jsonify({"data": 0})  
