from cmath import log
from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import current_user, login_required
from . import main

from..import db
from flask_login import login_required,current_user
from .forms import PostsForm, CommentForm
from ..models import User,Share,Comment,Post
import markdown2


#Index file or our home file
@main.route('/')
def index():

    return render_template('index.html')

#Posts/user stories form
@main.route('/share-story',methods=['GET', 'POST'])
@login_required
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

# all the posts/user stories
@main.route('/stories')
def posts():
    posts = Post.query.order_by(Post.addition_time.desc()).all()

    return render_template('stories.html', posts=posts)


#single posts
@main.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def single_story(post_id):
    
    user_story=Post.query.filter_by(id=post_id).first()
    # user_story =Post.query.get(id)
    print(user_story)
    if user_story is None:
        abort(404)
    format_user_story = markdown2.markdown(user_story.post_content,extras=["code-friendly", "fenced-code-blocks"])
    print(user_story.post_content)
    return render_template('single.html',user_story=user_story, format_user_story=format_user_story)

@main.route('/comment/<post_id>', methods=['GET', 'POST'])
# @login_required
def make_comment(post_id):
    user_comments = Comment.query.filter_by(post_id=post_id).all()
    post = Post.query.get(post_id)
    form = CommentForm()
    #If blog does not exist
    if post is None:
        abort(404)
    if form.validate_on_submit():
            comment = Comment(comment_Message=form.content.data,post_id=post_id,
            user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            #Reset form after submitting comment
            form.content.data = ''
            return redirect(url_for('main.posts'))
    return render_template('comment.html',post= post, user_comments =user_comments, form = form)

@main.route('/post/<id>')
def post(id):
    comments = Comment.query.filter_by(post_id=id).all()
    post = Post.query.get(id)
    return render_template('post.html',post=post,comments=comments)

@main.route('/about')
def about():


    return render_template('about.html')




