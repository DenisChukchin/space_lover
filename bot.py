import os
from dotenv import load_dotenv
import telegram


def send_message():
    bot.send_message(chat_id=chat_id, text='Hi John!')


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token)
    send_message()
    print(bot.get_me())
    updates = bot.get_updates()
    print(updates[0])
