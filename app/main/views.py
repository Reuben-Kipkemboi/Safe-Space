from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from..import db
# from flask_login import login_required,current_user
from .forms import PostsForm
from ..models import User,Share,Comment,Post

# from flask_login import login_required,current_user

@main.route('/')
def index():


    return render_template('index.html')

#Posts form
@main.route('/create_posts')
def new_posts():
    form = PostsForm()
    if form.validate_on_submit():
        
    
        
        return redirect(url_for('main.index'))
        
    
    return render_template('posts.html',form = form)