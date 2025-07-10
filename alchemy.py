from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    book_id = Column('book_id', Integer, primary_key=True)
    title = Column('title', String)
    author_name = Column('author_name', String)
    pages = Column('pages', Integer)
    reading_time = Column('reading_time', Integer)

    def __init__(self, book_id, title, author_name, pages, reading_time):
        self.book_id = book_id
        self.title = title
        self.author_name = author_name
        self.pages = pages
        self.reading_time = reading_time

    def __repr__(self):
        return f'({self.book_id}, {self.title}, {self.author_name}, {self.pages}, {self.reading_time})'


engine = create_engine("sqlite:///books.sqlite3", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

book = Book(1, 'Belladonna', 'Adalyn Grace', 400, 15)
session.add(book)
session.commit()

b1 = Book(2, 'Diune', 'Frank Herbert', 600, 40)
b2 = Book(3, 'Normal People', 'Sally Rooney', 250, 35)
b3 = Book(4, 'Bride', 'Ali Hazelwood', 390, 22)

session.add(b1)
session.add(b2)
session.add(b3)
session.commit()

