from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from petcompanyblog import db
from petcompanyblog.models import User, BlogPost
from petcompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from petcompanyblog.users.picture_handler import add_profile_pic 


users = Blueprint('users', __name__)

#Registration
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash("Welcome aboard!")

        return redirect(url_for('users.login'))
    
    return render_template('register.html', form=form)


#Login
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Login Success!')

            next = request.args.get('next')

            if next is None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next)
        
    return render_template('login.html', form=form)


#Logout
@users.rout('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))