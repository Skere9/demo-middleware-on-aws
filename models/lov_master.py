#
# User model
#

from sqlalchemy import Column, Integer, String

from models.model import Model 

class LovMaster(Model):
    __tablename__ = 'lov_master'

    id = Column(Integer, primary_key=True)
    lov_master_category = Column(String)

    def serialize(self):
        return {
            "id": self.id, 
            "lov_master_category": self.lov_master_category
            }

    #def __repr__(self):
    #   return "Userr('id'='%d', 'firstName'='%s', 'lastName'='%s', 'category'='%s')" % (
    #                        self.id, self.firstName, self.lastName, self.category)

#
# End
#
