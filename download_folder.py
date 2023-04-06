import os


def create_folder():
    """Создаем папку для фотографий"""
    if not os.path.exists("Images"):
        return os.makedirs("Images")


if __name__ == "__main__":
    create_folder()
