import os

from dotenv import load_dotenv

load_dotenv()


def mapbox_token(request):
    return {"mapbox_token": os.environ.get("MAPBOX_ACCESS_TOKEN")}
