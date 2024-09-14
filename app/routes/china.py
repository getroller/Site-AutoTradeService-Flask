from flask import Blueprint, render_template


china = Blueprint('china', __name__)


@china.route('/china')

def china_page ():
    return render_template('main/china.html')