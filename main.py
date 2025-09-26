# web_interface.py
from flask import Flask, request, render_template, redirect, url_for
from bot import TelegramBotHandler

app = Flask(__name__)
bot_handler = TelegramBotHandler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    message_text = request.form.get('message')
    success = bot_handler.send_message_to_group(message_text)
    if success:
        return redirect(url_for('index'))
    else:
        return "Ошибка отправки сообщения.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)