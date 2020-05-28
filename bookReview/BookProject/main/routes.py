from flask import Blueprint, render_template, redirect, flash
from BookProject.main.form import Search
from flask_login import current_user
from BookProject import db
from BookProject.models import Book

main = Blueprint('main', __name__)

@main.route('/', methods=['GET','POST'])
def home():
    form = None
    books = None
    if current_user.is_authenticated:
        form = Search()
        if form.validate_on_submit():
            data = form.query.data
            if form.select.data=="isbn":
                books = Book.query.filter(Book.isbn.like(f'%{data}%')).all()
            elif form.select.data=="author":
                books = Book.query.filter(Book.author.like(f'%{data}%')).all()
            elif form.select.data=="title":
                books = Book.query.filter(Book.title.like(f'%{data}%')).all()
            if books==[]:
                flash('There is no matching results!', category='warning')
    return render_template('home.html', form=form, books=books)

 

