import requests
import os
import argparse
from urllib.parse import urlparse, unquote
from dotenv import load_dotenv
from download_function import download_photo


def get_urls_nasa_pictures(token, photo_count):
    """Получаем ссылки на фотографии дня с сайта NASA"""
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": f"{token}",
        "count": photo_count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    photos = response.json()
    pictures = []
    for photo in photos:
        picture = photo.get("url")
        if picture.startswith("https://apod.nasa.gov"):
            pictures.append(picture)
    return pictures


def get_extension_from_file(url):
    """Получаем расширение фото из ссылки"""
    encode_link = unquote(url, encoding="utf-8", errors="replace")
    chopped_link = urlparse(encode_link)
    return os.path.splitext(chopped_link.path)[1]


def fetch_apod_nasa_pictures(urls_with_pictures):
    """Скачиваем фотографии дня с сайта NASA"""
    for number, photo in enumerate(urls_with_pictures):
        name_template = ["nasa_apod_", str(number), get_extension_from_file(photo)]
        filename = "".join(name_template)
        download_photo(photo, filename)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Скачиваем фотографии дня с сайта NASA"
    )
    parser.add_argument("count", type=int,
                        help="Введите количество фото для закачки, "
                             "иначе закачаю 5 фотографий",
                        default=5, nargs="?", const=1,
                        metavar="Целое число")
    args = parser.parse_args()
    return args


def main():
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    photo_count = parse_args().count
    try:
        urls_with_pictures = get_urls_nasa_pictures(token, photo_count)
        fetch_apod_nasa_pictures(urls_with_pictures)
    except requests.exceptions.HTTPError as error:
        print(error)


if __name__ == "__main__":
    main()
