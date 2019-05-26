#
# Award model
#

from sqlalchemy import Column, Integer, String

from models.model import Model 

class Award(Model):
    __tablename__ = 'award'

    id = Column(Integer, primary_key=True)
    awardTitle = Column(String)
    awardDescription = Column(String)
    awardPoints = Column(Integer)
    awardAuthor = Column(String)
    awardCreatedDate = Column(String)
    awardUpdatedDate = Column(String)
    awardCreatedBy = Column(String)
    awardUpdatedBy = Column(String)
 
    def serialize(self):
        return {
            "id": self.id, 
            "awardTitle": self.awardTitle, 
            "awardDescription": self.awardDescription, 
            "awardPoints": self.awardPoints,
            "awardAuthor": self.awardAuthor,
            "awardCreatedDate": self.awardCreatedDate,
            "awardUpdatedDate": self.awardUpdatedDate,
            "awardCreatedBy": self.awardCreatedBy, 
            "awardUpdatedBy": self.awardUpdatedBy
            }

#
# End
#
