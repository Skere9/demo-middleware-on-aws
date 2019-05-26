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

from models.blogpost import Blogpost
from dao.middleware import get_blogpost
from dao.middleware import get_blogposts
from dao.middleware import add_blogpost
from dao.middleware import mod_blogpost 
from dao.middleware import rem_blogpost 

from models.user import User
from dao.middleware import get_user
from dao.middleware import get_users
from dao.middleware import add_user
from dao.middleware import mod_user
from dao.middleware import rem_user

from dao.middleware import get_signin

from models.award import Award
from dao.middleware import get_award
from dao.middleware import get_awards
from dao.middleware import add_award
from dao.middleware import mod_award
from dao.middleware import rem_award

from models.lov_master import LovMaster
from dao.middleware import get_lov_master
from dao.middleware import get_lov_masters
from dao.middleware import add_lov_master
from dao.middleware import mod_lov_master
from dao.middleware import rem_lov_master

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
        newCustomer.email = customerData['p_email']
        newCustomer.subscribe = customerData['p_subscribe']
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
        newCustomer.email = customerData['p_email']
        newCustomer.subscribe = customerData['p_subscribe']
        newCustomer.category = customerData['p_category']
        mod_customer(newCustomer) 
        return jsonify({"data":"5"})

    @cross_origin()
    def delete(self, customer_id):
        # delete a single customer
        print('Customer API: delete a single customer')
        theResult = rem_customer(customer_id)
        return theResult 

class BlogpostAPI(MethodView):

    @cross_origin()
    def get(self, blogpost_id):
        if blogpost_id is None:
            # return a list of blogposts
            print('Blogpost API: return a list of blogposts')
            theResult = get_blogposts()
            return theResult 
        else:
            # expose a single blogpost
            print('Blogpost API: return a single blogpost')
            theResult = get_blogpost(blogpost_id)
            return theResult 

    @cross_origin()
    def post(self):
        # create a new blogpost
        print('Blogpost API: create a new blogpost')
        # print(type(json.dumps(request.data)))
        print('1')
        requestData = request.get_data().decode('utf8')
        print('2')
        blogpostData = json.loads(requestData)
        print('3')
        newBlogpost = Blogpost()
        print('4')
        newBlogpost.postDate = blogpostData['p_post_date']
        print('5')
        newBlogpost.title = blogpostData['p_title']
        print('6')
        newBlogpost.postContent = blogpostData['p_post_content']
        print('7')
        newBlogpost.keywords = blogpostData['p_keywords']
        print('8')
        newBlogpost.createDate = blogpostData['p_create_date']
        print('9')
        add_blogpost(newBlogpost)
        # TODO: Finish this section, then do "def put()"
        return jsonify({"Saved": True})

    @cross_origin()
    def put(self):
        # update a single blogpost
        print('Blogpost API: update a single blogpost')
        requestData = request.get_data().decode('utf8')
        blogpostData = json.loads(requestData)        
        newBlogpost = Blogpost()
        newBlogpost.id = blogpostData['p_customer_id']
        newBlogpost.postDate = blogpostData['p_post_date']
        newBlogpost.title = blogpostData['p_title']
        newBlogpost.postContent = blogpostData['p_post_content']
        newBlogpost.keywords = blogpostData['p_keywords']
        newBlogpost.createDate = blogpostData['p_create_date']
        mod_blogpost(newBlogpost) 
        return jsonify({"data":"5"})

    @cross_origin()
    def delete(self, blogpost_id):
        # delete a single blogpost
        print('Blogpost API: delete a single blogpost')
        theResult = rem_blogpost(blogpost_id)
        return theResult         

class UserAPI(MethodView):

    @cross_origin()
    def get(self, user_id):
        if user_id is None:
            # return a list of users
            print('User API: return a list of users')
            theResult = get_users()
            return theResult 
        else:
            # expose a single user
            print('User API: return a single user')
            theResult = get_user(user_id)
            return theResult 

    @cross_origin()
    def post(self):
        # create a new user
        print('User API: create a new user')
        requestData = request.get_data().decode('utf8')
        userData = json.loads(requestData)
        newUser = User()
        newUser.firstName = userData['p_first_name']
        newUser.lastName = userData['p_last_name']
        newUser.email = userData['p_email']
        newUser.emailValidated = userData['p_email_validated']
        newUser.accountStatus = userData['p_account_status']
        newUser.username = userData['p_username']
        newUser.password = userData['p_password']
        newUser.bio = userData['p_bio']
        newUser.subscribe = userData['p_subscribe']
        newUser.category = userData['p_category']
        newUser.role = userData['p_role']
        add_user(newUser)
        # TODO: Finish this section, then do "def put()"
        return jsonify({"Saved": True})

    @cross_origin()
    def put(self):
        # update a single user
        print('User API: update a single user')
        requestData = request.get_data().decode('utf8')
        userData = json.loads(requestData)        
        newUser = User()
        newUser.id = userData['p_user_id']
        newUser.firstName = userData['p_first_name']
        newUser.lastName = userData['p_last_name']
        newUser.email = userData['p_email']
        newUser.emailValidated = userData['p_email_validated']
        newUser.accountStatus = userData['p_account_status']
        newUser.username = userData['p_username']
        newUser.password = userData['p_password']
        newUser.bio = userData['p_bio']
        newUser.subscribe = userData['p_subscribe']
        newUser.category = userData['p_category']
        newUser.role = userData['p_role']
        mod_user(newUser) 
        return jsonify({"data":"5"})

    @cross_origin()
    def delete(self, user_id):
        # delete a single user
        print('User API: delete a single user')
        theResult = rem_user(user_id)
        return theResult   

class AwardAPI(MethodView):

    @cross_origin()
    def get(self, award_id):
        if award_id is None:
            # return a list of awards
            print('Award API: return a list of awards')
            theResult = get_awards()
            return theResult 
        else:
            # expose a single award
            print('Award API: return a single award')
            theResult = get_award(award_id)
            return theResult 

    @cross_origin()
    def post(self):
        # create a new award
        print('Award API: create a new award')
        requestData = request.get_data().decode('utf8')
        awardData = json.loads(requestData)
        newAward = Award()
        newAward.awardTitle = awardData['p_award_title']
        newAward.awardDescription = awardData['p_award_description']
        newAward.awardPoints = awardData['p_award_points']
        newAward.awardAuthor = awardData['p_award_author']
        newAward.awardCreatedDate = awardData['p_award_created_date']
        newAward.awardUpdatedDate = awardData['p_award_updated_date']
        newAward.awardCreatedBy = awardData['p_award_created_by']
        newAward.awardUpdatedBy = awardData['p_award_updated_by']
        add_award(newAward)
        # TODO: Finish this section, then do "def put()"
        return jsonify({"Saved": True})

    @cross_origin()
    def put(self):
        # update a single award
        print('Award API: update a single award')
        requestData = request.get_data().decode('utf8')
        awardData = json.loads(requestData)        
        newAward = Blogpost()
        newAward.awardTitle = awardData['p_award_title']
        newAward.awardDescription = awardData['p_award_description']
        newAward.awardPoints = awardData['p_award_points']
        newAward.awardAuthor = awardData['p_award_author']
        newAward.awardCreatedDate = awardData['p_award_created_date']
        newAward.awardUpdatedDate = awardData['p_award_updated_date']
        newAward.awardCreatedBy = awardData['p_award_created_by']
        newAward.awardUpdatedBy = awardData['p_award_updated_by']
        mod_award(newAward) 
        return jsonify({"data":"5"})

    @cross_origin()
    def delete(self, award_id):
        # delete a single award
        print('Award API: delete a single award')
        theResult = rem_award(award_id)
        return theResult   

class LovMasterAPI(MethodView):

    @cross_origin()
    def get(self, lov_master_id):
        print('Entering class lovMasterId - get()')
        print(lov_master_id)
        if lov_master_id is None:
            # return a list of LovMaster records
            print('LovMaster API: return a list of LovMaster records')
            theResult = get_lov_masters()
            return theResult 
        else:
            # expose a single LovMaster record
            print('LovMaster API: return a single LovMaster record')
            theResult = get_lov_master(lov_master_id)
            return theResult 

    @cross_origin()
    def post(self):
        # create a new LovMaster
        print('LovMaster API: create a new LovMaster record')
        requestData = request.get_data().decode('utf8')
        lovMasterData = json.loads(requestData)
        newLovMaster = LovMaster()
        newLovMaster.lov_master_category = lovMasterData['p_lov_master_category']
        print('TEST TEST TEST ')
        print(newLovMaster.lov_master_category)
        print('END TEST END TEST END TEST')
        add_lov_master(newLovMaster)
        # TODO: Finish this section, then do "def put()"
        return jsonify({"Saved": True})

    @cross_origin()
    def put(self):
        # update a single LovMaster
        print('LovMaster API: update a single LovMaster record')
        requestData = request.get_data().decode('utf8')
        lovMasterData = json.loads(requestData)        
        newLovMaster = LovMaster()
        newLovMaster.lovMasterCategory = lovMasterData['p_lov_master_category']
        mod_lov_master(newLovMaster) 
        return jsonify({"data":"5"})

    @cross_origin()
    def delete(self, lov_master_id):
        # delete a single LovMaster
        print('LovMaster API: delete a single LovMaster record')
        theResult = rem_lov_master(lov_master_id)
        return theResult   

class SignInAPI(MethodView):

    @cross_origin()
    def post(self):
        print('In SignIn GET:')
        requestData = request.get_data().decode('utf8')
        signInData = json.loads(requestData)        
        username = signInData['username']
        password = signInData['password']
        print(username)
        print(password)
        print('Those are the username nand password')
        if username is None:
            print('No username')
            return '-1'
        elif password is None:
            print('No password')
            return '-1'
        else:
            # Check login status
            # TODO: Implement login logic
            theResult = get_signin(username, password)
            return theResult 

def api_map(app):
    print(app.url_map)
    return jsonify({'data':'response is a map'})

def declare_api_routes(app):

    customer_view = CustomerAPI.as_view('customer_api')            
    app.add_url_rule('/api/customers/', defaults={'customer_id': None}, view_func=customer_view, methods=['GET',])
    app.add_url_rule('/api/customers',                                  view_func=customer_view, methods=['POST', 'PUT'])
    app.add_url_rule('/api/customers/<int:customer_id>',                view_func=customer_view, methods=['GET', 'DELETE'])

    blogpost_view = BlogpostAPI.as_view('blogpost_api')            
    app.add_url_rule('/api/blogposts/', defaults={'blogpost_id': None}, view_func=blogpost_view, methods=['GET',])
    app.add_url_rule('/api/blogposts',                                  view_func=blogpost_view, methods=['POST', 'PUT'])
    app.add_url_rule('/api/blogposts/<int:blogpost_id>',                view_func=blogpost_view, methods=['GET', 'DELETE'])

    user_view = UserAPI.as_view('user_api')
    app.add_url_rule('/api/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET',])
    app.add_url_rule('/api/users',                              view_func=user_view, methods=['POST', 'PUT'])
    app.add_url_rule('/api/users/<int:user_id>',                view_func=user_view, methods=['GET', 'DELETE'])

    signin_view = SignInAPI.as_view('signin_api')
    app.add_url_rule('/api/signin',                             view_func=signin_view, methods=['POST'])

    award_view = AwardAPI.as_view('award_api')
    app.add_url_rule('/api/awards/', defaults={'award_id': None}, view_func=award_view, methods=['GET',])
    app.add_url_rule('/api/awards',                               view_func=award_view, methods=['POST', 'PUT'])
    app.add_url_rule('/api/awards/<int:award_id>',                view_func=award_view, methods=['GET', 'DELETE'])
 
    lov_master_view = LovMasterAPI.as_view('lov_master_api')
    app.add_url_rule('/api/lov-masters/', defaults={'lov_master_id': None}, view_func=lov_master_view, methods=['GET',])
    app.add_url_rule('/api/lov-masters',                                    view_func=lov_master_view, methods=['POST', 'PUT'])
    app.add_url_rule('/api/lov-masters/<int:lov_master_id>',                view_func=lov_master_view, methods=['GET', 'DELETE'])

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

    def page_blogpost_list():
        theBlogposts = get_blogposts()
        theBlogposts = json.loads(theBlogposts.data)
        return render_template('blogpost_list.html', blogposts=theBlogposts)

    def page_award_list():
        theAwards = get_awards()
        theAwards = json.loads(theAwards.data)
        return render_template('award_list.html', awards=theAwards)

    def page_user_list():
        theUsers = get_users()
        theUsers = json.loads(theUsers.data)
        return render_template('user_list.html', users=theUsers)
    
    def page_lovmaster_list():
        theLovmasters = get_lov_masters()
        theLovmasters = json.loads(theLovmasters.data)
        return render_template('lovmaster_list.html', lovmasters=theLovmasters)

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
    app.add_url_rule('/blogpost-list', 'page_blogpost_list', page_blogpost_list, methods=['GET'])       
    app.add_url_rule('/award-list', 'page_award_list', page_award_list, methods=['GET'])    
    app.add_url_rule('/user-list', 'page_user_list', page_user_list, methods=['GET'])
    app.add_url_rule('/lovmaster-list', 'page_lovmaster_list', page_lovmaster_list, methods=['GET'])

    # ROUTES FOR FORMS FOR CUSTOMER - TESTING ONLY 

    def customer_form():
        print('Customer form')
        theTitle = 'Customer Entry Form'
        return render_template('customer_form.html', theTitle = theTitle)
    
    app.add_url_rule('/customer/form', 'customer_form', customer_form, methods=['GET'])
