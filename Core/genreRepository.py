from sqlalchemy import insert
from Core.models import genres
from Core.db import engine

def Create(name):
    command = insert(genres).values(name = name)
    with engine.connect() as connection:
        row_id = connection.execute(command)
        print(f"Добавлена запись с id={row_id.inserted_primary_key}")
        connection.commit()
