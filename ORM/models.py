from sqlalchemy import Table, Column, Integer, SmallInteger, Numeric, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from datetime import datetime

class Base(DeclarativeBase):
    pass

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name =  Column(String(50), nullable=False)
    books = relationship('Book', back_populates='genre')
    __table_args__ = (
        UniqueConstraint('name'),
    )

class Author_Book(Base):
    __tablename__ = 'author_book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer(), ForeignKey('authors.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'),nullable=False)

class User_Book(Base):
    __tablename__ = 'user_book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    year_of_issue = Column(Integer(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    genre_id = Column(Integer(), ForeignKey('genres.id'), nullable=False)
    genre = relationship('Genre', back_populates='books', uselist=False)
    authors = relationship('Author_Book', backref='authors')
    readers = relationship('User_Book', backref='users')

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    books = relationship('Author_Book', backref='books')
    __table_args__ = (
        UniqueConstraint('name'),
    )

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    readed_books = relationship('User_Book', backref='books')
    __table_args__ = (
        UniqueConstraint('name'),
        UniqueConstraint('email'),
    )



