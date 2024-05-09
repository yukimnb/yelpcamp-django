import os
import re
import sys
from pathlib import Path
from random import choice

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YelpCamp.settings.local")

import django
import requests
from dotenv import load_dotenv

load_dotenv()
django.setup()

from accounts.models import CustomUser
from campgrounds.models import Campground
from cities import cities
from django.conf import settings
from seedhelpers import descriptors, places


def main():
    # 全レコード削除
    Campground.objects.all().delete()

    # unsplashから画像取得
    while True:
        rest = 100 - current_count()
        response = get_unsplash_images()
        for content in response:
            if rest > 0:
                if save_images(content):
                    rest -= 1
            else:
                print("100枚の画像を保存しました")
                break

        if rest == 0:
            break

    # レコード作成
    records = []
    sample_author = CustomUser.objects.get(username="yuki")
    image_list = [*settings.MEDIA_ROOT.glob("*.jpg")]
    for _ in range(30):
        city = choice(cities)
        new_record = Campground(
            title=f"{choice(descriptors)}・{choice(places)}",
            price=choice(range(3000, 5001, 100)),
            location=city["prefecture"] + city["city"],
            geometry={
                "type": "Point",
                "coordinates": [city["longitude"], city["latitude"]],
            },
            description="\n".join(
                [
                    "Lorem ipsum dolor sit amet consectetur, adipisicing elit.",
                    "Provident illo, culpa similique ratione, exercitationem nam veritatis nostrum magnam soluta laborum aut rerum ea maiores sunt.",  # noqa
                    "Debitis ex consectetur commodi cupiditate!",
                ]
            ),
            image1=image_list.pop().name,
            image2=image_list.pop().name,
            image3=image_list.pop().name,
            author=sample_author,
        )
        records.append(new_record)
    Campground.objects.bulk_create(records)


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
        file_name = extract_word(content["alternative_slugs"]["en"])
    except AttributeError:
        return False
    file_path = settings.MEDIA_ROOT / file_name
    image_url = content["urls"]["regular"]
    if not check_for_existence(file_path):
        with open(file_path, "wb") as f:
            f.write(requests.get(image_url).content)
            return True
    else:
        return False


def extract_word(word):
    match_obj = re.match(r"(\S+)-", word)
    return match_obj.group(1) + ".jpg"


def check_for_existence(file_path):
    return file_path.exists()


def current_count():
    return len([*settings.MEDIA_ROOT.glob("*.jpg")])


if __name__ == "__main__":
    main()
