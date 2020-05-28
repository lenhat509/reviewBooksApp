from flask import Blueprint, render_template, redirect, flash, request
from BookProject.user.form import Registration, Login
from flask_login import current_user, login_required, login_user, logout_user
from BookProject import db, bcrypt
from BookProject.models import User, Book, Review

user = Blueprint('user', __name__)

@user.route('/register',methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    form = Registration()
    if form.validate_on_submit():
        data = User.query.filter_by(username = form.username.data).first()
        if data == None:
            hashpw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username = form.username.data, password = hashpw)
            db.session.add(user)
            db.session.commit()
            flash("Create a new account successfully!",category='success')
            return redirect('/login')
        else:
            form.username.errors.append('Username already exists in database')
    return render_template('register.html', form=form)

@user.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=False)
                flash("Login successfully!", category='success')
                next= request.args.get('next')
                if next:
                    return redirect(next)
                else: 
                    return redirect('/')
            else:
                form.password.errors.append("Wrong password!")
        else:
            form.username.errors.append("Username does not exist!")
    return render_template('login.html', form=form)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout successfully!", category='success')
    return redirect('/')