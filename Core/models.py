from sqlalchemy import Table, String, Integer, Column, Text, Boolean, ForeignKey, UniqueConstraint, ForeignKeyConstraint, DateTime
from datetime import datetime

metadata = MetaData()

genres = Table('genres', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(50), nullable=False),
    UniqueConstraint('name', name='unique_name')
)

books = Table('books', metadata,
    Column('id', Integer(), primary_key=True),
    Column('title', String(200), nullable=False),
    Column('year_of_issue', Integer(), nullable=False),
    Column('genre_id', Integer(), ForeignKey(genres.c.id), nullable=False)
    #Column('genre_id', ForeignKey('genres.id'), nullable=False) # или так
    #Column('genre_id', Integer(), nullable=False), # или так
    #ForeignKeyConstraint(['genre_id'], ['genres.id'])
)

users = Table('users', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(50), nullable=False),
    Column('Email', String(50), nullable=False),
    UniqueConstraint('name', name='unique_name')
)

book_user = Table('book_user', metadata,
    Column('user_id', Integer(), ForeignKey(users.c.id), nullable=False),
    Column('book_id', Integer(), ForeignKey(books.c.id), nullable=False)
)

authors = Table('authors', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(100), nullable=False),
    UniqueConstraint('name', name='unique_name')
)

author_book = Table('author_book', metadata,
    Column('author_id', Integer(), ForeignKey(authors.c.id), nullable=False),
    Column('book_id', Integer(), ForeignKey(books.c.id), nullable=False)
)