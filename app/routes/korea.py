from flask import Blueprint, render_template


korea = Blueprint('korea', __name__)


@korea.route('/korea')

def korea_page ():
    return render_template('main/korea.html')