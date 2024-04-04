import os
import sys
from pathlib import Path
from random import choice

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YelpCamp.settings")

import django
import requests
from dotenv import load_dotenv

django.setup()
load_dotenv()

from accounts.models import CustomUser
from campgrounds.models import Campground
from cities import cities
from seedhelpers import descriptors, places


def get_images():
    url = "https://api.unsplash.com/photos/random"
    config = {
        "collections": 483251,
        "client_id": os.environ.get("UNSPLASH_ACCESS_KEY"),
        "orientation": "landscape",
    }
    response = requests.get(url, config).json()
    res_image = response["urls"]["small"]

    return res_image


# 全レコード削除
Campground.objects.all().delete()
# レコード作成
records = []
sample_author = CustomUser.objects.get(username="yuki")
for _ in range(20):
    city = choice(cities)
    new_record = Campground(
        title=f"{choice(descriptors)}・{choice(places)}",
        price=choice(range(3000, 5001, 100)),
        location=city["prefecture"] + city["city"],
        description="\n".join(
            [
                "Lorem ipsum dolor sit amet consectetur, adipisicing elit.",
                "Provident illo, culpa similique ratione, exercitationem nam veritatis nostrum magnam soluta laborum aut rerum ea maiores sunt.",  # noqa
                "Debitis ex consectetur commodi cupiditate!",
            ]
        ),
        image=get_images(),
        author=sample_author,
    )
    records.append(new_record)
Campground.objects.bulk_create(records)
