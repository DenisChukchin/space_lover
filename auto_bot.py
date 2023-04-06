import os
import argparse
from dotenv import load_dotenv
import time
import telegram


def auto_send_pictures():
    """Бесконечный цикл по отправке фото"""
    while True:
        for root, dirs, files in os.walk("Images"):
            for file_name in files:
                with open(os.path.join("Images", file_name), "rb") as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(bot_timer)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Через какое время опубликовать фотографию боту"
    )
    parser.add_argument("timer", type=int,
                        help="Введите время в секундах. "
                             "По умолчанию задержка выставлена в 4 часа.",
                        default=14400,
                        nargs="?", const=1,
                        metavar="Время в секундах")
    parser.add_argument("-my_time", action="store_const",
                        const=my_timer, default=False,
                        help="Установить время публикации фотографий"
                             " через переменную окружения."
                             " Достаточно ввести '-my_time'.")
    args = parser.parse_args()
    if not args.my_time:
        return args.timer
    else:
        return args.my_time


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    my_timer = int(os.getenv('BOT_TIMER'))
    bot = telegram.Bot(token)
    bot_timer = parse_args()
    try:
        auto_send_pictures()
    except ValueError:
        print("Проверь вводимые данные!")
