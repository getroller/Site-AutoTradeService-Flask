from flask import Blueprint, render_template


japan = Blueprint('japan', __name__)


@japan.route('/japan')

def japan_page ():
    return render_template('main/japan.html')