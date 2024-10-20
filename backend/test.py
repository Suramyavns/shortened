from database import *
from models import *

obj = db_session.get(urls,1)
data = ids(url_id=obj.id)
db_session.add(data)
db_session.commit()
