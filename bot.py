import os
from dotenv import load_dotenv
import telegram


def send_document():
    bot.send_document(chat_id=chat_id, document=open("Images/spacex_2.jpg", "rb"))


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token)
    send_document()
