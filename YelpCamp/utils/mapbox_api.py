import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_forward_geocoding(address):
    url = "https://api.mapbox.com/search/geocode/v6/forward"
    config = {
        "q": address,
        "access_token": os.environ.get("MAPBOX_ACCESS_TOKEN"),
        "limit": 1,
    }

    return requests.get(url, config).json()["features"][0]["geometry"]
