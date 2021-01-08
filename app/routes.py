from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User
from flask import Flask, render_template, request, redirect, Response, url_for, session, abort, g, flash
from app.forms.forms import LoginForm, RegistrationForm


@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

@app.route("/")
@app.route("/Home")
@app.route("/home")
@login_required
def home():
        title="Yeet The Meat"
        return render_template('index.html',title=title,  BlogTitle="Test")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
        logout_user()
        return redirect(url_for('home'))