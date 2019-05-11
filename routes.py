#
# Initialize routes
#

from flask_cors import CORS, cross_origin

from flask import render_template
from flask import jsonify
from flask import request 
from flask.views import MethodView
import json 

from models.customer import Customer 
from dao.middleware import get_customer
from dao.middleware import get_customers
from dao.middleware import add_customer
from dao.middleware import mod_customer 
from dao.middleware import rem_customer 

class CustomerAPI(MethodView):

    @cross_origin()
    def get(self, customer_id):
        if customer_id is None:
            # return a list of customers
            print('Customer API: return a list of customers')
            theResult = get_customers()
            return theResult 
        else:
            # expose a single customer
            print('Customer API: return a single customer')
            theResult = get_customer(customer_id)
            return theResult 

    @cross_origin()
    def post(self):
        # create a new customer
        print('Customer API: create a new customer')
        # print(type(json.dumps(request.data)))
        requestData = request.get_data().decode('utf8')
        customerData = json.loads(requestData)
        newCustomer = Customer()
        newCustomer.firstName = customerData['p_first_name']
        newCustomer.lastName = customerData['p_last_name']
        newCustomer.category = customerData['p_category']
        add_customer(newCustomer)
        # TODO: Finish this section, then do "def put()"
        return jsonify({"Saved": True})

    @cross_origin()
    def put(self):
        # update a single customer
        print('Customer API: update a single customer')
        requestData = request.get_data().decode('utf8')
        customerData = json.loads(requestData)        
        newCustomer = Customer()
        newCustomer.id = customerData['p_customer_id']
        newCustomer.firstName = customerData['p_first_name']
        newCustomer.lastName = customerData['p_last_name']
        newCustomer.category = customerData['p_category']
        mod_customer(newCustomer) 
        return jsonify({"data":"5"})

    @cross_origin()
    def delete(self, customer_id):
        # delete a single customer
        print('Customer API: delete a single customer')
        theResult = rem_customer(customer_id)
        return theResult 

def api_map(app):
    print(app.url_map)
    return jsonify({'data':'response is a map'})

def declare_api_routes(app):

    customer_view = CustomerAPI.as_view('customer_api')            
    app.add_url_rule('/api/customers/', defaults={'customer_id': None}, view_func=customer_view, methods=['GET',])
    app.add_url_rule('/api/customers',                                  view_func=customer_view, methods=['POST', 'PUT'])
    app.add_url_rule('/api/customers/<int:customer_id>',                view_func=customer_view, methods=['GET', 'DELETE'])

    # app.add_url_rule('/api/customer/<string:pCustomerId>',
    #                                    'get_customer',  get_customer,  methods=['GET'])
    # app.add_url_rule('/api/customers', 'get_customers', get_customers, methods=['GET'])
    # app.add_url_rule('/api/customer',  'add_customer',  add_customer,  methods=['POST'])
    # app.add_url_rule('/api/customer',  'mod_customer',  mod_customer,  methods=['PUT'])
    # app.add_url_rule('/api/customer/<string:pCustomerId>', 
    #                                     'rem_customer',  rem_customer,  methods=['DELETE'])

    # ROUTES FOR ADMIN 

    def page_home():
        theTitle = 'It worked!'
        return render_template('home.html', theTitle = theTitle)

    def page_form():
        theTitle = 'Customer form'
        return render_template('form.html', theTitle = theTitle)

    def page_about():
        theTitle = 'About this app'
        return render_template('about.html', theTitle = theTitle)

    def page_api():
        theTitle = 'This is the API branch'
        return render_template('api.html', theTitle = theTitle)        

    app.add_url_rule('/',      'page_home',  page_home,  methods=['GET'])
    app.add_url_rule('/form',  'page_form',  page_form,  methods=['GET'])
    app.add_url_rule('/about', 'page_about', page_about, methods=['GET'])    
    app.add_url_rule('/api',   'page_api',   page_api,   methods=['GET'])
    app.add_url_rule('/api/',  'page_api',   page_api,   methods=['GET'])    

    # ROUTES FOR FORMS FOR CUSTOMER - TESTING ONLY 

    def customer_form():
        print('Customer form')
        theTitle = 'Customer Entry Form'
        return render_template('customer_form.html', theTitle = theTitle)
    
    app.add_url_rule('/customer/form', 'customer_form', customer_form, methods=['GET'])
