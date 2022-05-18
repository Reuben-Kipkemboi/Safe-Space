
  
from crypt import methods
from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required
from . import main
# from ..requests import 
from .forms import PostForm
from ..models import User, Post
# from .. import db,photos

# from flask_login import login_required,current_user

@main.route('/')
def index():


    return render_template('index.html')

@main.route('/about')
def about():


    return render_template('about.html')

@main.route('/stories')
def stories():


    return render_template('stories.html')

@main.route('/write/new', methods= ['GET', 'POST'])
def new_write():
    form = PostForm()
    if form.validate_on_submit ():
        poster_name = form.name.data
        post_content = form.message.data

        #update review instance
        new_blog = Post(poster_name = poster_name, post_content= post_content)


        #save review methods
        new_blog.save_blog()
        return redirect (url_for('main.blog'))

    else: all_posts = Post.query.order_by(Post.posted).all


    return render_template('form.html',blog_form = form, posts = all_posts)  


