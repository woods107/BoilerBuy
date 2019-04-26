from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm
from app.forms import RegisterForm
from app.forms import SubmitForm
from app.models import User, Post
from werkzeug.urls import url_parse

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
    # check if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # else if username accepted
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # if user not exists or pass not correct
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # user is correct and password is correct
        login_user(user)
#        next_page = request.args.get('next')
#        if not next_page or url_parse(next_page).netloc != '':
#            next_page = url_for('index')
#        return redirect(url_for(next_page))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Account registered for user {} with email {}'.format(
            form.username.data, form.email.data))
            # TODO: Add check to see that user doesn not already exist
        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    form = SubmitForm()
    if form.validate_on_submit():
        flash('Submission \'{}\' made successfully'.format(
            form.title.data))
        p = Post(title=form.title.data, body=form.body.data, user_id=current_user.id, uname=current_user.username, contact=current_user.email)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
