from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField,TextAreaField
from wtforms.validators import DataRequired
from ..models import User,Post,Comment,Share


class PostsForm(FlaskForm):
    title = StringField('Enter your Post Title', validators=[DataRequired()])
    author = StringField('Post Author Name',validators=[DataRequired()])
    # blog_category = RadioField('Blog Category :', choices = [('Technology', 'Technology'),  ('Lifestyle', ' Lifestyle'), ('Farming', 'Farming'),('Vehicles & Transport' , 'Vehicles and Transport'), ('Fashion and Clothing', 'Fashion & Clothing', ('Education', 'Education'))], validators = [DataRequired()])
    content = TextAreaField('Your Personal Story')
    submit = SubmitField('Make A Post')