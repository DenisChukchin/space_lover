import os
import random
import argparse
from dotenv import load_dotenv
import telegram


def parse_args():
    parser = argparse.ArgumentParser(
        description="Отправляем одно случайное фото по названию файла, "
                    "например, epic_planet_0.png или nasa_apod_1.jpg "
                    "или spacex_3.jpg"
    )
    parser.add_argument("picture", type=str,
                        help="Введите название файла с фото, "
                             "иначе отправлю случайное фото",
                        default=random.choice(os.listdir("Images")),
                        nargs="?", const=1,
                        metavar="Название файла с расширением")
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token)
    random_picture = parse_args().picture
    try:
        with open(f"Images/{random_picture}", "rb") as file:
            bot.send_document(chat_id=chat_id, document=file)
    except FileNotFoundError:
        print("Не существует такого файла, попробуй снова.")


if __name__ == "__main__":
    main()
