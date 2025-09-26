# telegram_bot.py

from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_GROUP_CHAT_ID

class TelegramBotHandler:
    def __init__(self):
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)

    def send_message_to_group(self, message):
        """
        Отправляет сообщение в Telegram группу.
        :param message: Текст сообщения
        """
        try:
            self.bot.send_message(chat_id=TELEGRAM_GROUP_CHAT_ID, text=message)
            return True
        except Exception as e:
            print(f"Ошибка отправки сообщения: {e}")
            return False