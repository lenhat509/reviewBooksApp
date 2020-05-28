from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import EqualTo, DataRequired, Length


class Registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=8, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100)])
    confirm = PasswordField('Confirm', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Submit')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=8, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100)])
    submit = SubmitField('Submit')