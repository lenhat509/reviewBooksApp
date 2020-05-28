from flask import Blueprint, render_template, redirect, flash
from BookProject.book.form import Reviews
from flask_login import current_user, login_required
from BookProject import db
from BookProject.config import dic
from BookProject.models import Book, Review
import requests


books=Blueprint('books', __name__)

@books.route('/book/<int:id>', methods=['GET', 'POST'])
@login_required
def book(id):
    book = Book.query.get_or_404(id)
    goodReads = 'Not available from GoodReads'
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={'key': dic['API_KEY'], 'isbns': [book.isbn]})
    if res.status_code == 200:
        data= res.json()
        goodReads = f"(The average rating: {data['books'][0]['average_rating']}, with {data['books'][0]['ratings_count']} ratings from GoodReads)"
    form = Reviews()
    if Review.query.filter(Review.user_id==current_user.id, Review.book_id==book.id).first():
        form = None
    if form and form.validate_on_submit():
        review = Review(user_id=current_user.id, book_id=id, rating= form.rating.data, comment= form.comment.data)
        db.session.add(review)
        db.session.commit()
        form = None
        flash('Thank you for your rating!',category='success')
    return render_template('book.html', book=book, title='Book Page', form = form, goodReads=goodReads)