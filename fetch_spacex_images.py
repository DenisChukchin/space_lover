import argparse
import requests
from download_function import download_photo


def fetch_spacex_last_launch(flight_number):
    """Скачиваем фото с запуска шатла"""
    base_url = f"https://api.spacexdata.com/v3/launches/{flight_number}"
    response = requests.get(base_url)
    response.raise_for_status()
    urls_with_photos = response.json()["links"]["flickr_images"]
    for number, photo in enumerate(urls_with_photos):
        name_template = ["spacex_", str(number), ".jpg"]
        filename = "".join(name_template)
        download_photo(photo, filename)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Скачиваем фото с запуска шатла SpaceX"
    )
    parser.add_argument("flight_number", type=int,
                        help="Введите номер полета, "
                             "например, любое от 60 до 100. "
                             "Если не знаете номер, "
                             "скрипт скачает фото с последнего запуска",
                        default=107, nargs="?", const=1,
                        metavar="Целое число")
    args = parser.parse_args()
    return args


def main():
    flight_number = parse_args().flight_number
    try:
        fetch_spacex_last_launch(flight_number)
        print("Если запрос прошел, а фотографии не загрузились "
              "- значит фотографии с этим запуском шатла отсутвуют на сайте!")
    except requests.exceptions.HTTPError as error:
        print(error, "\nТакой страницы не существует, попробуй другой запуск.")


if __name__ == "__main__":
    main()
