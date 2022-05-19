
from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from app.models import User,Post,Comment,Subscriber

from .. import db

from flask_login import login_required,current_user
# from ..email import mail_message
import secrets
import os
 
from flask import render_template,request,redirect,url_for,abort,flash
from . import main


@main.route('/')
def index():


    return render_template('index.html')

@main.route('/comment/<post_id>', methods = ['Post','GET'])
@login_required
def comment(post_id):
    post = post.query.get(post_id)
    comment =request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, post_id=post_id)
    new_comment.save()
    return redirect(url_for('main.post',id = post.id))
@main.route('/post/<id>')
def post(id):
    comments = Comment.query.filter_by(post_id=id).all()
    post = post.query.get(id)
    return render_template('post.html',post=post,comments=comments)