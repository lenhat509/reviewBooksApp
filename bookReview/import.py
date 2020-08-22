import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("Import your own database uri")
db = scoped_session(sessionmaker(bind=engine))
file = open('books.csv', "r")

def main():
    csv_file = csv.DictReader(file)
    for obj in csv_file:
        db.execute("INSERT INTO book(isbn, author, title, year) values(:isbn,:author,:title,:year)", {"isbn":obj['isbn'], "author":obj['author'], "title":obj['title'], "year":obj['year']})
    db.commit()

if __name__=="__main__":
    main()
