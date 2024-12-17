from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

# Create a Blueprint
main = Blueprint('main', __name__)

# Define a route for the home page
@main.route('/')
def home():
    return render_template("index.jinja2")

# Define a route for the profile page
@main.route('/profile')
@login_required
def profile():
    return render_template("profile.jinja2", name=current_user.name)

# Define a route for the data tracking page
@main.route('/data')
@login_required
def data():
    return render_template("data.jinja2")
