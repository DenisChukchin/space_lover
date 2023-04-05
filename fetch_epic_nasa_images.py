import requests
import os
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv
from download_folder import create_folder


def epic_nasa_pictures():
    """Скачиваем фотографии Земли сделанные 2 дня назад"""
    two_days_ago = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{two_days_ago}"
    params = {
        "api_key": f"{token}"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    photos = response.json()
    for number, photo in enumerate(photos[:count_of_photos]):
        days_ago = (datetime.now() - timedelta(days=2)).strftime("%Y/%m/%d")
        photo_url = ("""https://api.nasa.gov/EPIC/archive/natural/"""
                     f"""{days_ago}/png/{photo.get("image")}"""
                     f""".png?api_key={token}""")
        generate_name = ["epic_planet_", str(number), ".png"]
        filename = "".join(generate_name)
        with open("Images/{}".format(filename), 'wb') as file:
            file.write(requests.get(photo_url).content)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Скачиваем фото Земли с сайта NASA, "
                    "полученные два дня назад"
    )
    parser.add_argument("count", type=int,
                        help="Введите количество фото, "
                             "которые будут закачены "
                             "(Всего можно скачать 13 фотографий). "
                             "Иначе скачаю 5 фотографий.",
                        default=5, nargs="?", const=1,
                        metavar="Целое число")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    create_folder()
    count_of_photos = parse_args().count
    epic_nasa_pictures()
