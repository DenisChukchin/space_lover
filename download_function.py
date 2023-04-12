import requests
import os


def download_photo(photo, filename, params=None):
    os.makedirs("Images", exist_ok=True)
    photo_response = requests.get(photo, params=params)
    photo_response.raise_for_status()
    with open("Images/{}".format(filename), 'wb') as file:
        file.write(photo_response.content)
