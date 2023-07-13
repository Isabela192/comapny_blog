from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from flask_login import current_user
from petcompanyblog.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_field = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('passwd_confirm', message='Passwords must Match!')])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('You are already registered')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('You are already registered')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken')    