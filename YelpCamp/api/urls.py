from django.urls import path

from .views import (
    CampgroundListCreateAPIView,
    CampgroundRetrieveUpdateDestroyAPIView,
    CustomUserCreateAPIView,
    CustomUserDestroyAPIView,
)

app_name = "apiv1"
urlpatterns = [
    path("campgrounds/", CampgroundListCreateAPIView.as_view()),
    path("campgrounds/<id>/", CampgroundRetrieveUpdateDestroyAPIView.as_view()),
    path("accounts/", CustomUserCreateAPIView.as_view()),
    path("accounts/<id>/", CustomUserDestroyAPIView.as_view()),
]
