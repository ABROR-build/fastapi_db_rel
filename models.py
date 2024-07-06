from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
    reviews = relationship("Reviews", back_populates="user")


class Author(Base):
    __tablename__ = "Author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    year = Column(String, index=True)

    book_author = relationship('BookAuthor', back_populates="author")


class BookAuthor(Base):
    __tablename__ = "BookAuthor"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("Author.id"))
    book = relationship("Books", back_populates="book_author")

    author = relationship("Author", back_populates="book_author")


class Categories(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True, index=True)

    category = relationship("Books", back_populates="category")


class Books(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True, index=True)

    category = Column(String, index=True)
    name = relationship("Categories", back_populates="category")

    category_id = Column(Integer, ForeignKey("Categories.id"))
    author_id = Column(Integer, ForeignKey("Author.id"))
    description = Column(String, index=True)
    ISBN = Column(String, index=True)
    price = Column(Integer, index=True)
    date = Column(DateTime, index=True)

    reviews = relationship("Reviews", back_populates="book")


class Reviews(Base):
    __tablename__ = "Reviews"

    id = Column(Integer, primary_key=True, index=True)
    star_given = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    user = relationship("Users", back_populates="reviews")
    book_id = Column(Integer, ForeignKey("Books.id"))
    book = relationship("Books", back_populates="reviews")
