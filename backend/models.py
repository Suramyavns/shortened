'''
This module specifies the entities and their attributes for the database
'''
import uuid as v4
from sqlalchemy import Column, Integer, String,UUID,ForeignKey
from database import Base

class Urls(Base):
    '''
    This entity will store url along with a primary key
    '''
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(10000))

    def __init__(self, id=None, url=None):
        self.id = id
        self.url = url

    def __repr__(self):
        return f'<URL {self.url} >'

class IDs(Base):
    '''
    This entity will store the IDs of each URL mapped to a UUID for security reasons
    '''
    __tablename__='ids'
    uuid = Column(UUID(as_uuid=True),primary_key=True,default=v4.uuid4)
    id = Column(Integer,ForeignKey('urls.id'),nullable=False)

    def __init__(self, uuid=None,url_id=None):
        self.uuid = uuid
        self.id = url_id

    def __repr__(self):
        return f'<ID {self.uuid} >'
