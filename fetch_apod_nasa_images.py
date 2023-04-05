import requests
import os
from urllib.parse import urlparse, unquote
from dotenv import load_dotenv
from download_folder import create_folder


def get_urls_nasa_pictures():
    """Получаем ссылки на фотографии дня с сайта NASA"""
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": f"{token}",
        "count": 5
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    get_photos = response.json()
    pictures = []
    for photos in get_photos:
        picture = photos.get("url")
        if picture.startswith("https://apod.nasa.gov"):
            pictures.append(picture)
        elif picture.endswith(".html"):
            pass
    return pictures


def get_extension_from_file():
    """Получаем расширение фотографий"""
    extensions = []
    for picture in urls_with_pictures:
        encode_link = unquote(picture, encoding="utf-8", errors="replace")
        chopped_link = urlparse(encode_link)
        extensions.append(os.path.splitext(chopped_link.path)[1])
    return extensions


def fetch_apod_nasa_pictures():
    """Скачиваем фотографии дня с сайта NASA"""
    photos_with_extense = list(zip(urls_with_pictures, extense))
    for number, photo in enumerate(photos_with_extense):
        generate_name = ["nasa_apod_", str(number), photo[1]]
        filename = "".join(generate_name)
        with open("Images/{}".format(filename), 'wb') as file:
            file.write(requests.get(photo[0]).content)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')
    create_folder()
    get_urls_nasa_pictures()
    urls_with_pictures = get_urls_nasa_pictures()
    get_extension_from_file()
    extense = get_extension_from_file()
    fetch_apod_nasa_pictures()
