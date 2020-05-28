from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import  DataRequired, Length


class Search(FlaskForm):
    select = SelectField('Search by', choices=[("isbn", "ISBN"),('title', 'Title'),('author', "Author")], validators=[DataRequired()])
    query = StringField('Search', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Submit')