#
# User model
#

from sqlalchemy import Column, Integer, String

from models.model import Model 

class LovEntity(Model):
    __tablename__ = 'lov_entities'

    id = Column(Integer, primary_key=True)
    lov_master_id = Column(Integer)
    lov_value = Column(String)
    lov_sort_order = Column(Integer)

    def serialize(self):
        return {
            "id": self.id, 
            "lov_master_id": self.lov_master_id,
            "lov_value": self.lov_value,
            "lov_sort_order": self.lov_sort_order
            }

    #def __repr__(self):
    #   return "Userr('id'='%d', 'firstName'='%s', 'lastName'='%s', 'category'='%s')" % (
    #                        self.id, self.firstName, self.lastName, self.category)

#
# End
#
