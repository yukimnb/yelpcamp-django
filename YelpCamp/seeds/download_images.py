import os
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import requests
from dotenv import load_dotenv

load_dotenv()

from YelpCamp.settings import MEDIA_ROOT


def main():
    for _ in range(50):
        response = get_unsplash_images()
        for content in response:
            if not has_100_files():
                save_images(content)
            else:
                print("100枚の画像を保存しました")
                sys.exit()


def get_unsplash_images():
    url = "https://api.unsplash.com/photos/random"
    config = {
        "collections": 483251,
        "client_id": os.environ.get("UNSPLASH_ACCESS_KEY"),
        "orientation": "landscape",
        "count": 30,
    }
    return requests.get(url, config).json()


def save_images(content):
    try:
        file_name = extract_word(content["alternative_slugs"]["ja"])
    except AttributeError:
        return
    file_path = MEDIA_ROOT / file_name
    image_url = content["urls"]["regular"]
    if not check_for_existence(file_path):
        with open(file_path, "wb") as f:
            f.write(requests.get(image_url).content)


def extract_word(word):
    match_obj = re.match(r"(\S+?)-", word)
    return match_obj.group(1) + ".jpg"


def check_for_existence(file_path):
    return file_path.exists()


def has_100_files():
    return len([*MEDIA_ROOT.glob("*.jpg")]) >= 100


if __name__ == "__main__":
    main()
