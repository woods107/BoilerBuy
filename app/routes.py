from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from app.forms import RegisterForm
from app.models import User, Post

@app.route('/')
@app.route('/index')
def index():
    #Use placeholder dummy list of posts for the moment
    #User object will contain username, real name, and contact info fields (eventually)
    #Posts will contain title, description, posting date, object of user, and a photo
    postings = Post.query.all()#= []
    return render_template('index.html', postings=postings)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Account registered for user {} with email {}'.format(
            form.username.data, form.email.data))
            # TODO: Add check to see that user doesn not already exist
        u = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)
