#
# User model
#

from sqlalchemy import Column, Integer, String

from models.model import Model 

class User(Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    emailValidated = Column(String)
    accountStatus = Column(String)
    username = Column(String)
    password = Column(String)
    bio = Column(String)
    subscribe = Column(String)
    category = Column(String)
    role = Column(String)
    timezone = Column(String)
    language = Column(String)
    picture = Column(String)

    def serialize(self):
        return {
            "id": self.id, 
            "firstName": self.firstName, 
            "lastName": self.lastName, 
            "email": self.email,
            "emailValidated": self.emailValidated,
            "accountStatus": self.accountStatus,
            "username": self.username,
            "password": self.password,
            "bio": self.bio, 
            "subscribe": self.subscribe,
            "category": self.category,
            "role": self.role,
            "timezone": self.timezone,
            "language": self.language,
            "picture": self.picture
            }

    #def __repr__(self):
    #   return "Userr('id'='%d', 'firstName'='%s', 'lastName'='%s', 'category'='%s')" % (
    #                        self.id, self.firstName, self.lastName, self.category)

#
# End
#
