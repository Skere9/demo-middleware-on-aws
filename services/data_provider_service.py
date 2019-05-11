#
# File: data_provider_service.py 
#

from sqlalchemy.orm import sessionmaker 
from contextlib import contextmanager 
import configparser
from sqlalchemy import create_engine
from models.model import Model 

class DbServer:

    session = -1 

    def __init__(self):
        self.initialize_database()
        pass 

    def load_sample_data(self):
        buyer_1 = Customer() 
        buyer_1.firstName = 'Joe'
        DbServer.session.add(buyer_1)
        DbServer.session.commit()
        print('Starting FOR loop ...')
        for row in DbServer.session.query(Customer, Customer.firstName).all():
            print(row.Customer, row.firstName)
        print('Done')

    # 
    # End class
    # 

class DbConnectService():

    the_db_sessionmaker = None 

    def __init__(self):
        self.the_db_connection_string_created = False
        self.the_db_engine = self.getTheDbEngine()
        Model.metadata.create_all(self.the_db_engine)
        DbConnectService.the_db_sessionmaker = sessionmaker(bind=self.the_db_engine)

    def getTheDbEngine(self):
        print('Entering initialize_database')
        if not self.the_db_connection_string_created:
            print('Instantiating session')
            config = configparser.ConfigParser()
            config.read('properties.ini')
            theDataSource = config['Settings']['the_database']
            if theDataSource == 'SQLite':
                self.the_db_engine_connection_string = 'sqlite:///demo.db'
            else:
                theDatabase_connection_string = '{db_product}://{username}:{password}@{hostname}:{port}/{database}'
                theDb_product = config[theDataSource]['db_product']
                theUsername = config[theDataSource]['username']
                thePassword = config[theDataSource]['password']
                theHostname = config[theDataSource]['hostname']
                thePort = config[theDataSource]['port']
                theDatabase = config[theDataSource]['database']
                self.the_db_engine_connection_string = theDatabase_connection_string.format(
                    db_product=theDb_product,
                    username=theUsername,
                    password=thePassword,
                    hostname=theHostname,
                    port=thePort,
                    database=theDatabase
                )
        return create_engine(self.the_db_engine_connection_string)

@contextmanager
def session_scope():
    session = DbConnectService.the_db_sessionmaker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        session.close()
        raise
    finally:
        session.close()
