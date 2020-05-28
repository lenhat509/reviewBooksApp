from flask import Blueprint, render_template, redirect, flash, jsonify
from BookProject import db
from BookProject.config import dic
from BookProject.models import Book, Review
from sqlalchemy import func

apis=Blueprint('apis', __name__)
 
@apis.route('/api/<string:isbn>', methods=["GET"])
def getBook(isbn): 
    book = Book.query.filter_by(isbn=isbn).first()
    if book:
        count = Review.query.filter_by(book_id=book.id).count()
        average = 0
        if count!=0 :
            average = round(float(db.session.query(func.avg(Review.rating)).filter(Review.book_id == book.id).first()[0]) , 2)
        api = {'title':book.title, 'author': book.author, 'year': book.year, 'isbn':book.isbn, 'review_count':count, 'average_score':average}
        return jsonify(api)
    else:
        return jsonify({'status_code':404,'error':'No matching ISBN'})