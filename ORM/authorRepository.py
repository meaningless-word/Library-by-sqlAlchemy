from ORM.models import Author
from ORM.db import Session

def Create(item):
    with Session() as session:
        session.add(item)
        session.commit()