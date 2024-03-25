from django.urls import path

from .views import CreateCampground, DetailCampground, EditCampground, ListCampground

app_name = "campgrounds"
urlpatterns = [
    path("", ListCampground.as_view(), name="list"),
    path("<int:id>/", DetailCampground.as_view(), name="detail"),
    path("create/", CreateCampground.as_view(), name="create"),
    path("<int:id>/edit/", EditCampground.as_view(), name="edit"),
]
