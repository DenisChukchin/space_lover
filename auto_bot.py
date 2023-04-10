import os
import argparse
from dotenv import load_dotenv
import time
import telegram


def auto_send_pictures(bot, chat_id, bot_timer):
    """Бесконечный цикл по отправке фото"""
    while True:
        for root, dirs, files in os.walk("Images"):
            for file_name in files:
                with open(os.path.join("Images", file_name), "rb") as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(bot_timer)


def parse_args(user_timer):
    parser = argparse.ArgumentParser(
        description="Через какое время опубликовать фотографию боту"
    )
    parser.add_argument("timer", type=int,
                        help="Введите время в секундах. "
                             "По умолчанию задержка выставлена в 4 часа.",
                        default=14400,
                        nargs="?", const=1,
                        metavar="Время в секундах")
    parser.add_argument("-user_timer", action="store_const",
                        const=user_timer, default=False,
                        help="Установить время публикации фотографий"
                             " через переменную окружения."
                             " Достаточно ввести '-user_timer'.")
    args = parser.parse_args()
    if not args.user_timer:
        return args.timer
    else:
        return args.user_timer


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    user_timer = int(os.getenv('BOT_TIMER'))
    bot = telegram.Bot(token)
    bot_timer = parse_args(user_timer)
    try:
        auto_send_pictures(bot, chat_id, bot_timer)
    except ValueError:
        print("Проверь вводимые данные!")


if __name__ == "__main__":
    main()
