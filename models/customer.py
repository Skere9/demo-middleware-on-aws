#
# Customer model
#

from sqlalchemy import Column, Integer, String

from models.model import Model 

class Customer(Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    category = Column(String)

    def serialize(self):
        return {
            "id": self.id, 
            "firstName": self.firstName, 
            "lastName": self.lastName, 
            "category": self.category
            }

    #def __repr__(self):
    #   return "Customer('id'='%d', 'firstName'='%s', 'lastName'='%s', 'category'='%s')" % (
    #                        self.id, self.firstName, self.lastName, self.category)

#
# End
#
