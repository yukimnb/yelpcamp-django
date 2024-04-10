import os
import sys
from pathlib import Path
from random import choice

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YelpCamp.settings")

import django

django.setup()

from accounts.models import CustomUser
from campgrounds.models import Campground
from cities import cities
from seedhelpers import descriptors, places

from YelpCamp.settings import MEDIA_ROOT


def main():
    # 全レコード削除
    Campground.objects.all().delete()
    # レコード作成
    records = []
    sample_author = CustomUser.objects.get(username="yuki")
    image_list = [*MEDIA_ROOT.glob("*.jpg")]
    for _ in range(30):
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
            image1=image_list.pop().name,
            image2=image_list.pop().name,
            image3=image_list.pop().name,
            author=sample_author,
        )
        records.append(new_record)
    Campground.objects.bulk_create(records)


if __name__ == "__main__":
    main()
