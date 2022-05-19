from flask_wtf import FlaskForm



from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField,TextAreaField
from wtforms.validators import DataRequired
from ..models import User,Post,Comment,Share


class PostsForm(FlaskForm):
    title = StringField('Enter your Post Title', validators=[DataRequired()])
    author = StringField('Post Author Name',validators=[DataRequired()])
    content = TextAreaField('Your Personal Story')
    submit = SubmitField('Make A Post')

