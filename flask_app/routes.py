from flask import current_app as app
from flask import render_template, request, redirect, url_for, session

@app.route('/')
def home():
    return render_template('index.jinja2')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('login.jinja2')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.jinja2')

@app.route('/profile')
def profile():
    return render_template('profile.jinja2')