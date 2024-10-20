from sqlalchemy import Column, Integer, String,UUID,ForeignKey
from database import Base
import uuid as v4
from sqlalchemy.orm import relationship

class urls(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(10000), unique=True)

    def __init__(self, id=None, url=None):
        self.id = id
        self.url = url

    def __repr__(self):
        return f'<URL {self.url} >'
    
class ids(Base):
    __tablename__='ids'
    uuid = Column(UUID(as_uuid=True),primary_key=True)
    id = Column(Integer,ForeignKey('urls.id'),nullable=False)

    def __init__(self, uuid=v4.uuid1(),url_id=None):
        self.uuid = uuid
        self.id = url_id

    def __repr__(self):
        return f'<URL {self.url} >'