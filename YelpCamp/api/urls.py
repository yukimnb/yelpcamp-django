from django.urls import include, path

from .views import (
    CampgroundListCreateAPIView,
    CampgroundRetrieveUpdateDestroyAPIView,
    CustomUserCreateAPIView,
)

app_name = "apiv1"
urlpatterns = [
    path("campgrounds/", CampgroundListCreateAPIView.as_view()),
    path("campgrounds/<id>/", CampgroundRetrieveUpdateDestroyAPIView.as_view()),
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/", CustomUserCreateAPIView.as_view()),
]
