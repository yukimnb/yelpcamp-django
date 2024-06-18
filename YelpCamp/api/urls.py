from django.urls import include, path

from .views import (
    CampgroundListCreateAPIView,
    CampgroundRetrieveUpdateDestroyAPIView,
)

app_name = "apiv1"
urlpatterns = [
    path("campgrounds/", CampgroundListCreateAPIView.as_view()),
    path("campgrounds/<id>/", CampgroundRetrieveUpdateDestroyAPIView.as_view()),
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/signup/", include("dj_rest_auth.registration.urls")),
]
