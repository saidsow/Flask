from flask import Blueprint, render_template

# Create a Blueprint
main = Blueprint('main', __name__)

# Define a route for the home page
@main.route('/')
def home():
    return render_template("index.jinja2")
