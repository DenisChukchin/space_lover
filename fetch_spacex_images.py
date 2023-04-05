import argparse
import requests
from download_folder import create_folder


def fetch_spacex_last_launch():
    base_url = f"https://api.spacexdata.com/v3/launches/{flight_number}"
    response = requests.get(base_url)
    response.raise_for_status()
    urls_with_photos = response.json()["links"]["flickr_images"]
    for number, photo in enumerate(urls_with_photos):
        generate_name = ["spacex_", str(number), ".jpg"]
        filename = "".join(generate_name)
        with open("Images/{}".format(filename), 'wb') as file:
            file.write(requests.get(photo).content)


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


if __name__ == "__main__":
    create_folder()
    flight_number = parse_args().flight_number
    fetch_spacex_last_launch()
