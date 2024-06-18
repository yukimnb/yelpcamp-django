from accounts.models import CustomUser
from campgrounds.models import Campground
from rest_framework import serializers


class CampgroundSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Campground
        fields = [
            "id",
            "title",
            "price",
            "location",
            "geometry",
            "description",
            "image1",
            "image2",
            "image3",
            "author",
            "author_name",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]
