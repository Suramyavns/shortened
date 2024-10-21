from database import *
from models import *
from uuid import UUID
import validators

def add_url(url):
    if validators.url(url):
        obj = urls(url=url)
        db_session.add(obj)
        db_session.flush()
        data = ids(url_id=obj.id)
        db_session.add(data)
        db_session.flush()
        db_session.commit()
        return data.uuid
    return None

def get_url(uuid):
    try:
        urlid = db_session.get(ids,UUID(uuid))
    except:
        return None
    else:
        if urlid:
            urlobj = db_session.get(urls,urlid.id)
            return urlobj.url
        return None