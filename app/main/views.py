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
@main.route('/share-story',methods=['GET', 'POST'])
def new_posts():
    form = PostsForm()
    if form.validate_on_submit():
        title = form.title.data
        post_content = form.content.data
        author_name = form.author.data
        new_user_post= Post(title=title, post_content=post_content, author_name =  author_name)
        
        new_user_post.save_posts()
    
        return redirect(url_for('main.index'))
    return render_template('posts.html',form = form)


@main.route('/posts')
def posts():
    posts = Post.query.order_by(Post.addition_time.desc()).all()

    return render_template('overall.html', posts=posts)

