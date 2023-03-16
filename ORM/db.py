from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ORM.models import *

# строка подключения
sqlite_database = 'sqlite:///library.db'

# создаём движок SqlAlchemy
engine = create_engine(sqlite_database, echo=True)

# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаём класс сессии
Session = sessionmaker(autoflush=False, bind=engine)
