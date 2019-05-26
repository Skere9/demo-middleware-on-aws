#
# File: middleware.py
#

import json 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import request 
from flask import jsonify
from flask.views import View
from sqlalchemy import and_ 

import mailchimp

from services.data_provider_service import DbConnectService
from services.data_provider_service import session_scope 
from models.model import Model 
from models.customer import Customer 
from models.blogpost import Blogpost
from models.user import User
from models.award import Award 
from models.lov_master import LovMaster
from models.lov_entity import LovEntity

# UTILITIES FOR APIs

def load_initial_data():
    with session_scope() as s:
        totalUserRecords = s.query(User).count()
        if totalUserRecords == 0:
            user_1 = User() 
            user_1.firstName = 'Steve'
            user_1.lastName = 'OHearn'
            user_1.email = 'soh@databasetraining.com'
            user_1.accountStatus = 'ACTIVE'
            user_1.username = 'Skere'
            user_1.password = 'Skere'
            user_1.bio = 'Creator of the DatabaseTraining.com site.'
            user_1.role = 'ADMIN'
            user_1.language = 'English'
            s.add(user_1)
            lov_master_1 = LOV_Master()
            lov_master_1.lov_master_category = 'Role'
            the_pk = s.add(lov_master_1)
            lov_entity_1 = LOV_Entity()
            lov_entity_1.lov_master_id = the_pk
            lov_entity_1.lov_value = 'VISITOR'
            lov_entity_1.lov_sort_order = 1
            s.add(lov_category_1)
            lov_entity_2 = LOV_Entity()
            lov_entity_2.lov_master_id = the_pk
            lov_entity_2.lov_value = 'REGISTERED'
            lov_entity_2.lov_sort_order = 2
            s.add(lov_category_2)
            lov_entity_3 = LOV_Entity()
            lov_entity_3.lov_master_id = the_pk
            lov_entity_3.lov_value = 'ADMIN'
            lov_entity_3.lov_sort_order = 3
            s.add(lov_category_3)                        
            s.commit()
            print('Starting FOR loop ...')
            theResults = s.query(User, User.firstName, User.lastName).all()
            for row in theResults:
                print(row.User, row.firstName)
            print('Initialization completed.')
        else:
            print('Already initialized at a prior time')

def transformQueryOutputToJson(pParameter):
    '''Transform queried data (pParameter)
    to jsonified output for sending via a REST interface.
    '''
    # Serialize the instances
    interimResult = [the_parm.serialize() for the_parm in pParameter]
    # Jsonify the list 
    return jsonify(interimResult)


# API for CUSTOMER

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
        # Determine if this new customer has elected to subscribe
        if (pCustomer.subscribe == 'Yes'):
            # Yes.  Therefore post to MailChimp
            print('SUBSCRIBE THIS CUSTOMER!')
            # TODO: Move these specific values to a properties.ini file.
            API_KEY = '2e68df53d0457c4b9ceb25bf34cf99d8-us20'
            LIST_ID = '06d4e253a8' 
            api = mailchimp.Mailchimp(API_KEY)
            try:
                api.lists.subscribe(LIST_ID, {'email': pCustomer.email})
                print('DONE!')
            except:
                print('ERROR!')

            #MAILCHIMP_SIGNUP_URL = 'https://corbinian.us20.list-manage.com/subscribe/post?u=cc1f637aebedc431bca68ebb2&amp;id=06d4e253a8'
            #PARAMS = {'email':'new@corbinian.com', 'b_cc1f637aebedc431bca68ebb2_06d4e253a8': ''} 
            #try:
            #    r = requests.post(url = MAILCHIMP_SIGNUP_URL, params = PARAMS) 
            #except:
            #    print('ERROR!')
            ## pastebin_url = r.text 
            ## print("The pastebin URL is:%s"%pastebin_url)


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


# API for BLOGPOST

def get_blogpost(pBlogpostId, serialize=True):
    # This is the API to return a single blogpost with an ID of pBlogpostId
    with session_scope() as s:
        the_blogposts = []
        the_blogposts = s.query(Blogpost).filter(Blogpost.id == pBlogpostId).all()
        if serialize:
            return transformQueryOutputToJson(the_blogposts)
        else:
            return the_blogposts   

def get_blogposts(serialize=True):
    # This is the API to return all blogposts
    with session_scope() as s:
        the_blogposts = s.query(Blogpost).order_by(Blogpost.id).all()
        if serialize:
            return transformQueryOutputToJson(the_blogposts)
        else:
            return jsonify(the_blogposts)   

def add_blogpost(pBlogpost):
    theResponse = 'This is the API to add a new blogpost'
    with session_scope() as s: 
        the_result = s.add(pBlogpost)
        return the_result

def mod_blogpost(pBlogpost, serialize=True):
    theResponse = 'This is the API to update an existing blogpost'
    with session_scope() as s:
        print('The blogpost info is: ')
        print(pBlogpost.id)
        print(pBlogpost.postDate)
        print(pBlogpost.title)
        print(pBlogpost.postContent)
        print(pBlogpost.keywords)
        print(pBlogpost.createDate)
        print('That was it!')
        items_updated= s.query(Blogpost).filter(Blogpost.id == pBlogpost.id).update({
            Blogpost.postDate: pBlogpost.postDate,
            Blogpost.title: pBlogpost.title,
            Blogpost.postContent: pBlogpost.postContent,
            Blogpost.keywords: pBlogpost.keywords,
            Blogpost.createDate: pBlogpost.createDate
            }, synchronize_session=False)
        if items_updated > 0:
            return jsonify({"data": items_updated})
        else:
            return jsonify({"data": 0})  

def rem_blogpost(pBlogpostId, serialize=True):
    theResponse = 'This is the API to remove a single blogpost'
    print('The ID to delete is:')
    print(pBlogpostId)
    print('So let us see if that works.')
    with session_scope() as s:
        items_deleted = s.query(Blogpost).filter(Blogpost.id == pBlogpostId).delete()
        if items_deleted > 0:
            return jsonify({"data": items_deleted})
        else:
            return jsonify({"data": 0})  


# API for USER

def get_user(pUserId, serialize=True):
    # This is the API to return a single user with an ID of pUserId
    with session_scope() as s:
        the_users = []
        the_users = s.query(User).filter(User.id == pUserId).all()
        if serialize:
            return transformQueryOutputToJson(the_users)
        else:
            return the_users   

def get_users(serialize=True):
    # This is the API to return all users
    with session_scope() as s:
        the_users = s.query(User).order_by(User.id).all()
        if serialize:
            return transformQueryOutputToJson(the_users)
        else:
            return jsonify(the_users)   

def add_user(pUser):
    theResponse = 'This is the API to add a new user'
    with session_scope() as s: 
        the_result = s.add(pUser)
        return the_result

def mod_user(pUser, serialize=True):
    theResponse = 'This is the API to update an existing user'
    with session_scope() as s:
        print('The user info is: ')
        print(pUser.id)
        print(pUser.firstName)
        print(pUser.lastName)
        print(pUser.email)
        print(pUser.subscribe)
        print(pUser.category)
        print('That was it!')
        items_updated= s.query(User).filter(User.id == pUser.id).update({
            User.firstName: pUser.firstName,
            User.lastName: pUser.lastName,
            User.email: pUser.email,
            User.emailValidated: pUser.emailValidated,
            User.accountStatus: pUser.accountStatus,
            User.username: pUser.username,
            User.password: pUser.password,
            User.bio: pUser.bio,
            User.subscribe: pUser.subscribe,
            User.category: pUser.category,
            User.role: pUser.role 
            }, synchronize_session=False)
        if items_updated > 0:
            return jsonify({"data": items_updated})
        else:
            return jsonify({"data": 0})  

def rem_user(pUserId, serialize=True):
    theResponse = 'This is the API to remove a single user'
    print('The ID to delete is:')
    print(pUserId)
    print('So let us see if that works.')
    with session_scope() as s:
        items_deleted = s.query(User).filter(User.id == pUserId).delete()
        if items_deleted > 0:
            return jsonify({"data": items_deleted})
        else:
            return jsonify({"data": 0})  

# API for AWARD

def get_award(pAwardId, serialize=True):
    # This is the API to return a single award with an ID of pAwardId
    with session_scope() as s:
        the_awards = []
        the_awards = s.query(Award).filter(Award.id == pAwardId).all()
        if serialize:
            return transformQueryOutputToJson(the_awards)
        else:
            return the_awards

def get_awards(serialize=True):
    # This is the API to return all awards
    with session_scope() as s:
        the_awards = s.query(Award).order_by(Award.id).all()
        if serialize:
            return transformQueryOutputToJson(the_awards)
        else:
            return jsonify(the_awards)   

def add_award(pAward):
    theResponse = 'This is the API to add a new award'
    with session_scope() as s: 
        the_result = s.add(pAward)
        return the_result

def mod_award(pAward, serialize=True):
    theResponse = 'This is the API to update an existing award'
    with session_scope() as s:
        print('The award info is: ')
        print(pAward.id)
        print(pAward.userId)
        print(pAward.createdDate)
        print(pAward.lastLoginDate)
        print(pAward.status)
        print('That was it!')
        items_updated= s.query(Award).filter(Award.id == pAward.id).update({
            Award.awardTitle: pAward.awardTitle,
            Award.awardDescription: pAward.awardDescription,
            Award.awardPoints: pAward.awardPoints,
            Award.awardAuthor: pAward.awardAuthor,
            Award.awardCreatedDate: pAward.awardCreatedDate,
            Award.awardUpdatedDate: pAward.awardUpdatedDate,
            Award.awardCreatedBy: pAward.awardCreatedBy,
            Award.awardUpdatedBy: pAward.awardUpdatedBy
            }, synchronize_session=False)
        if items_updated > 0:
            return jsonify({"data": items_updated})
        else:
            return jsonify({"data": 0})  

def rem_award(pAwardId, serialize=True):
    theResponse = 'This is the API to remove a single award'
    print('The ID to delete is:')
    print(pAwardId)
    print('So let us see if that works.')
    with session_scope() as s:
        items_deleted = s.query(Award).filter(Award.id == pAwardId).delete()
        if items_deleted > 0:
            return jsonify({"data": items_deleted})
        else:
            return jsonify({"data": 0})  

# API for LOV_MASTER

def get_lov_master(pLovMasterId, serialize=True):
    # This is the API to return a single lov_master record with an ID of pLovMasterId
    with session_scope() as s:
        the_lov_masters = []
        the_lov_masters = s.query(LovMaster).filter(LovMaster.id == pLovMasterId).all()
        if serialize:
            return transformQueryOutputToJson(the_lov_masters)
        else:
            return the_lov_masters

def get_lov_masters(serialize=True):
    # This is the API to return all lov_masters
    with session_scope() as s:
        the_lov_masters = s.query(LovMaster).order_by(LovMaster.id).all()
        if serialize:
            return transformQueryOutputToJson(the_lov_masters)
        else:
            return jsonify(the_lov_masters)   

def add_lov_master(pLovMaster):
    theResponse = 'This is the API to add a new lov_master'
    with session_scope() as s: 
        the_result = s.add(pLovMaster)
        return the_result

def mod_lov_master(pLovMaster, serialize=True):
    theResponse = 'This is the API to update an existing lov_master'
    with session_scope() as s:
        print('The lovMaster info is: ')
        print(pLovMaster.id)
        print(pLovMaster.lov_master_category)
        print('That was it!')
        items_updated= s.query(LovMaster).filter(LovMaster.id == pLovMaster.id).update({
            LovMaster.lov_master_category: pLovMaster.lov_master_category
            }, synchronize_session=False)
        if items_updated > 0:
            return jsonify({"data": items_updated})
        else:
            return jsonify({"data": 0})  

def rem_lov_master(pLovMasterId, serialize=True):
    theResponse = 'This is the API to remove a single lov_master'
    print('The ID to delete is:')
    print(pLovMasterId)
    print('So let us see if that works.')
    with session_scope() as s:
        items_deleted = s.query(LovMaster).filter(LovMaster.id == pLovMasterId).delete()
        if items_deleted > 0:
            return jsonify({"data": items_deleted})
        else:
            return jsonify({"data": 0})  

# API for SIGNIN

def get_signin(username, password, serialize=True):
    # This is the API to sign in a user
    with session_scope() as s:
        print('Inside get_signin')
        signin_success = s.query(User).filter(and_(User.username == username, User.password == password)).all()
        if signin_success:
            if (signin_success[0].password == password):
                theResult = signin_success
            else:
                theResult = False  
        else:
            theResult = False  
        if theResult:
            if serialize:
                return transformQueryOutputToJson(theResult)
            else:
                return jsonify(theResult)
        else: 
            return jsonify(theResult)
