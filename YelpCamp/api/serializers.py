from accounts.models import CustomUser
from campgrounds.models import Campground
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class CampgroundSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Campground
        fields = [
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
