from campgrounds.models import Campground, Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.ReadOnlyField(source="reviewer.username")

    class Meta:
        model = Review
        fields = ["id", "comment", "rating", "campground", "reviewer", "reviewer_name"]


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
