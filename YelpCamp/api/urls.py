from django.urls import path

from .views import CampgroundListCreateAPIView, CampgroundRetrieveUpdateDestroyAPIView

app_name = "apiv1"
urlpatterns = [
    path("campgrounds/", CampgroundListCreateAPIView.as_view()),
    path("campgrounds/<id>/", CampgroundRetrieveUpdateDestroyAPIView.as_view()),
]
