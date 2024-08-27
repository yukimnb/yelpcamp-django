import os
import re
import sys
from pathlib import Path
from random import choice

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YelpCamp.settings.production")

import django
import requests
from dotenv import load_dotenv

load_dotenv()
django.setup()

from accounts.models import CustomUser
from campgrounds.models import Campground, Review
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
    print("キャンプ場を作成しました")

    # レビュー作成
    friends = CustomUser.objects.filter(username__in=["hiroki", "keiji", "akira", "kohei", "yuki"])

    records = []
    for campground in Campground.objects.all():
        for friend in friends:
            records.append(
                Review(
                    rating=choice(["3", "4", "5"]),
                    comment=choice(
                        [
                            "素晴らしい自然に囲まれて、心身ともにリフレッシュできました！",
                            "夜空の星がとても綺麗で、忘れられない思い出になりました。",
                            "設備が整っていて快適なキャンプ体験ができました！",
                            "スタッフの皆さんが親切で、安心して過ごせました。",
                            "焚き火を囲んで語り合う時間が最高でした。",
                            "子供たちも大満足！家族でまた来たいと思います。",
                            "美しい湖の景色が本当に素晴らしかったです。",
                            "自然の中でのんびりと過ごす時間が最高の贅沢です。",
                            "トイレも清潔で、女性でも安心して利用できました。",
                            "次回もぜひここでキャンプしたいと思います！",
                            "キャンプ場の雰囲気が最高で、癒される時間を過ごせました。",
                            "大自然の中で過ごす時間が、心に響きました。",
                            "設備が充実していて、快適なキャンプを楽しめました。",
                            "山の風景が美しく、まるで絵画のようでした。",
                            "夜の静寂が心地よく、ぐっすり眠れました。",
                            "バーベキューがとても美味しく、家族みんなが大満足でした。",
                            "スタッフの対応が素晴らしく、安心して過ごせました。",
                            "ハイキングコースが充実していて、自然を満喫できました。",
                            "清潔感があり、女性や子供にも優しいキャンプ場でした。",
                            "風の音と鳥のさえずりに癒される贅沢な時間でした。",
                        ]
                    ),
                    campground=campground,
                    reviewer=friend,
                )
            )
    Review.objects.bulk_create(records)
    print("レビューを作成しました")


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
