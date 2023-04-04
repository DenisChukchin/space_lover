import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote
from datetime import datetime, timedelta
load_dotenv()


def create_folder():
    """Создаем папку для фотографий"""
    if not os.path.exists("Images"):
        return os.makedirs("Images")


def fetch_spacex_last_launch():
    """Скачиваем фото с запуска шатла"""
    base_url = "https://api.spacexdata.com/v3/launches/65"
    response = requests.get(base_url)
    response.raise_for_status()
    urls_with_photos = response.json()["links"]["flickr_images"]
    for number, photo in enumerate(urls_with_photos):
        generate_name = ["spacex_", str(number), ".jpg"]
        filename = "".join(generate_name)
        with open("Images/{}".format(filename), 'wb') as file:
            file.write(requests.get(photo).content)


def get_urls_nasa_pictures():
    """Получаем ссылки на фотографии дня с сайта NASA"""
    token = os.getenv('NASA_TOKEN')
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


def get_extension_from_file(pics):
    """Получаем расширение фотографий"""
    extensions = []
    for pic in pics:
        encode_link = unquote(pic, encoding="utf-8", errors="replace")
        chopped_link = urlparse(encode_link)
        extensions.append(os.path.splitext(chopped_link.path)[1])
    return extensions


def fetch_apod_nasa_pictures(pics, extense):
    """Скачиваем фотографии дня с сайта NASA"""
    photos_with_extense = list(zip(pics, extense))
    for number, photo in enumerate(photos_with_extense):
        generate_name = ["nasa_apod_", str(number), photo[1]]
        filename = "".join(generate_name)
        with open("Images/{}".format(filename), 'wb') as file:
            file.write(requests.get(photo[0]).content)


def epic_nasa_pictures():
    """Скачиваем 5 фотографии Земли сделанные 2 дня назад"""
    two_days_ago = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    token = os.getenv('NASA_TOKEN')
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{two_days_ago}"
    params = {
        "api_key": f"{token}"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    photos = response.json()
    for number, photo in enumerate(photos[:5]):
        days_ago = (datetime.now() - timedelta(days=2)).strftime("%Y/%m/%d")
        photo_url = ("""https://api.nasa.gov/EPIC/archive/natural/"""
                     f"""{days_ago}/png/{photo.get("image")}"""
                     f""".png?api_key={token}""")
        generate_name = ["epic_planet_", str(number), ".png"]
        filename = "".join(generate_name)
        with open("Images/{}".format(filename), 'wb') as file:
            file.write(requests.get(photo_url).content)


def main():
    create_folder()
    fetch_spacex_last_launch()
    get_urls_nasa_pictures()
    pics = get_urls_nasa_pictures()
    get_extension_from_file(pics)
    extense = get_extension_from_file(pics)
    fetch_apod_nasa_pictures(pics, extense)
    epic_nasa_pictures()


if __name__ == "__main__":
    main()
