from flask import Blueprint, render_template


about = Blueprint('about', __name__)


@about.route('/about')

def about_page ():
    return render_template('main/about.html')