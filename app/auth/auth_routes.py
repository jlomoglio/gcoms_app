from flask import render_template, redirect, request, flash, url_for
from .auth_models import User, Task
from werkzeug.security import generate_password_hash, check_password_hash
from . import bp
from app import db  # Ensure you import your database instance correctly
from flask_login import login_user, logout_user, login_required, current_user
from .forms.login_form import LoginForm


@bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Logic for logging in the user
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Logged in successfully', category='success')
            login_user(user, remember=True)
            return redirect(url_for('dashboard.dashboard'))
        else:
            if not user:
                flash('User not found. Please check you email & password and try again.', category='error')
            elif password == '':
                flash('Your Password is required', category='error')
            elif not check_password_hash(user.password, password):
                flash('You entered an incorrect password', category='error')

    return render_template('auth.html', user=current_user, form=form)

@bp.route('/logout')
@login_required
def logout():
    # Logic for logging out the user
    flash('You have been signed out', category='success')
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/add-user', methods=['GET', 'POST'])
@login_required
def add_user():
    if request.method == 'POST':
        """ Get form data """
        username = request.form['username']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password1 = request.form['password1']
        password2 = request.form['password2']

        """ Validate form data """
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(username) < 2:
            flash('Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be at least 2 characters', category='error')
        elif len(last_name) < 7:
            flash('Last name must be at least 7 characters', category='error')
        else:
            """ Add user to the database """
            new_user = User(
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name,
                password = generate_password_hash(password1, method='scrypt')
            )
            db.session.add(new_user)
            db.session.commit()
            flash('User was added successfully', category='success')
            return redirect(url_for('auth.login'))
    return render_template('add_user.html', user=current_user)