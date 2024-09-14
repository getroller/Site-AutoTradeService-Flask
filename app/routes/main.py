from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mailman import EmailMessage
from ..config import Config

main = Blueprint('main', __name__)


@main.route('/')

def index ():
    return render_template('main/index.html')


@main.route('/send_email', methods=['POST'])
def send_email():

    name = request.form['name']
    number = request.form['number']
    city = request.form['city']

    msg = EmailMessage(
        subject="New Contact Form Submission",
        body=f"Имя: {name}\nНомер: {number}\nГород:{city}",
        to=[Config.MAIL_DEFAULT_SENDER]
    )



    try:
        msg.send()
        flash('Ваше сообщение успешно отправлено!', 'success')
    except Exception as e:
        flash(f'Ошибка при отправке сообщения: {e}', 'danger')

    return redirect(url_for('main.index'))