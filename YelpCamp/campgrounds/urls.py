from django.urls import path

from .views import (
    CreateCampground,
    CreateReview,
    DeleteCampground,
    DeleteReview,
    DetailCampground,
    EditCampground,
    ListCampground,
)

app_name = "campgrounds"
urlpatterns = [
    path("", ListCampground.as_view(), name="list"),
    path("<int:id>/", DetailCampground.as_view(), name="detail"),
    path("create/", CreateCampground.as_view(), name="create"),
    path("<int:id>/edit/", EditCampground.as_view(), name="edit"),
    path("<int:id>/delete/", DeleteCampground.as_view(), name="delete"),
    path("<int:id>/reviews/create/", CreateReview.as_view(), name="create_review"),
    path("<int:id>/reviews/<int:review_id>/delete/", DeleteReview.as_view(), name="delete_review"),
]
