from flask import current_app as app
from flask import render_template, request, redirect, url_for, session

@app.route('/')
def home():
    return render_template('index.jinja2')

@app.route('/login', methods=['POST'])
def login_page():
    username = request.form['username']
    session['username'] = username
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/test')
def test():
    return render_template('test.jinja2')

@app.route("/dashboard")
def dashboard():
    # Render a Jinja2 template that contains the embedded Dash app
    if not session.get("username"):
        return redirect(url_for("login"))
    return render_template("dashboard.jinja2")  # Jinja2 template for dashboard