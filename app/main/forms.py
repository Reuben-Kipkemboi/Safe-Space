from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField,TextAreaField
from wtforms.validators import DataRequired
from ..models import User,Post,Comment,Share


class BlogForm(FlaskForm):
    title = StringField('Enter your Blog Title', validators=[DataRequired()])
    author = StringField('Blog Author Name',)
    # blog_category = RadioField('Blog Category :', choices = [('Technology', 'Technology'),  ('Lifestyle', ' Lifestyle'), ('Farming', 'Farming'),('Vehicles & Transport' , 'Vehicles and Transport'), ('Fashion and Clothing', 'Fashion & Clothing', ('Education', 'Education'))], validators = [DataRequired()])
    content = TextAreaField('Blog content')
    submit = SubmitField('BLOG')