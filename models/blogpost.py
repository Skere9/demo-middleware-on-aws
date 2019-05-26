#
# Blogpost model
#

from sqlalchemy import Column, Integer, String

from models.model import Model 

class Blogpost(Model):
    __tablename__ = 'blogpost'

    id = Column(Integer, primary_key=True)
    postDate = Column(String)
    title = Column(String)
    postContent = Column(String)
    keywords = Column(String)
    createDate = Column(String)

    def serialize(self):
        return {
            "id": self.id, 
            "postDate": self.postDate,
            "title": self.title,
            "postContent": self.postContent,
            "keywords": self.keywords,
            "createDate": self.createDate
            }

    #def __repr__(self):
    #   return "Customer('id'='%d', 'firstName'='%s', 'lastName'='%s', 'category'='%s')" % (
    #                        self.id, self.firstName, self.lastName, self.category)

#
# End
#
