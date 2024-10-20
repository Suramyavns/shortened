from database import *
from models import *

def add_url(url):
    obj = urls(url=url)
    db_session.add(obj)
    db_session.flush()
    data = ids(url_id=obj.id)
    db_session.add(data)
    db_session.flush()
    return data.uuid

