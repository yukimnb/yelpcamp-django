import os
import sys
from pathlib import Path
from random import choice

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YelpCamp.settings")

import django

django.setup()

from campgrounds.models import Campground
from cities import cities
from seedhelpers import descriptors, places

# 全レコード削除
Campground.objects.all().delete()

# レコード作成
records = []
for _ in range(50):
    city = choice(cities)
    new_record = Campground(
        title=f"{choice(descriptors)}・{choice(places)}",
        price=choice(range(3000, 5001, 100)),
        description="\n".join(
            [
                "Lorem ipsum dolor sit amet consectetur, adipisicing elit.",
                "Provident illo, culpa similique ratione, exercitationem nam veritatis nostrum magnam soluta laborum aut rerum ea maiores sunt.",
                "Debitis ex consectetur commodi cupiditate!",
            ]
        ),
        location=city["prefecture"] + city["city"],
    )
    records.append(new_record)
Campground.objects.bulk_create(records)
