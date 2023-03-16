from ORM.models import Genre
from ORM.db import Session


def Create(item):
    with Session() as session:
        session.add(item)
        session.commit()

def Read(**kwargs):
    with Session() as session:
        if len(kwargs) == 0:
            return session.query(Genre.id, Genre.name).all()
        if "id" in kwargs:
            return session.query(Genre.id, Genre.name).filter(Genre.id == kwargs["id"]).first()

def Update(item):
    with Session() as session:
        g = session.query(Genre).filter(Genre.id == item.id).first()
        if g != None:
            g.name = item.name
            session.commit()

def Delete(item):
    with Session() as session:
        g = session.query(Genre).filter(Genre.id == item.id).first()
        session.delete(g)
        session.commit()