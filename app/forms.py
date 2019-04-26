from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    register = SubmitField('Register')


class SubmitForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    term = StringField('Search Terms')
    search = SubmitField('Search', validators=[DataRequired()])

