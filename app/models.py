#application models
#**********************models*****************
###user model
##comments model
## posts
## subscribers /share option
from datetime import datetime
from flask_login import UserMixin
from . import db
#securing user passwords
from werkzeug.security import generate_password_hash,check_password_hash

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

#Users table

class User( UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True) 
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    avatar = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    post_types = db.relationship('Pitch', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    
    #used to create a write only class property password
    @property
    def password(self):
        raise AttributeError('You are not allowed to read passcode')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'
      
#Post table
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post_content = db.Column(db.Text(), nullable = False)
    author_name = db.Column(db.String(255),nullable = False)
    addition_time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref='posts',lazy='dynamic')
    
    def save_posts(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_user_posts(cls,pitch_type_category):
        user_posts = Post.query.filter_by(category=Post.category).all()
        return user_posts
  
    def __repr__(self):
        return f'Post {self.post_content}'
    

#User comments table
class Comment(db.Model):
    __tablename__ = 'user_comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_Message = db.Column(db.Text(),nullable = False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'),nullable = False)

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        user_comments = Comment.query.filter_by(post_id=post_id).all()

        return user_comments
    
    
class Share(db.Model):
    __tablename__ = 'shares'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
      
    def save(self):
        db.session.add(self)
        db.session.commit()
  
