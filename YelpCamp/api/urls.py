from django.urls import include, path

from .views import (
    CampgroundListCreateAPIView,
    CampgroundRetrieveUpdateDestroyAPIView,
    CustomLoginView,
)

app_name = "apiv1"
urlpatterns = [
    path("campgrounds/", CampgroundListCreateAPIView.as_view()),
    path("campgrounds/<id>/", CampgroundRetrieveUpdateDestroyAPIView.as_view()),
    path("accounts/login/", CustomLoginView.as_view()),
    path("accounts/signup/", include("dj_rest_auth.registration.urls")),
    path("accounts/", include("dj_rest_auth.urls")),
]
