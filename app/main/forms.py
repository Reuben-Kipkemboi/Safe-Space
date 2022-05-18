from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField

class PostForm (FlaskForm):
    name = TextAreaField('Your name', validators=[DataRequired()])
    message = TextAreaField (validators=[DataRequired()])
    submit = SubmitField('Submit')