from sqlalchemy import create_engine, insert
from Core.models import *

engine = create_engine('sqlite:///library.db')
metadata.create_all(engine)
print(engine)
