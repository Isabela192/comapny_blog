import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
### DATABASE SETUP ####

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

### Login Setup ###
login_manger = LoginManager()
login_manger.init_app(app)
login_manger.login_view = 'users.login'

#### App Setup ###
from petcompanyblog.core.views import core
from petcompanyblog.error_pages.handlers import error_pages
from petcompanyblog.users.views import users
from petcompanyblog.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)