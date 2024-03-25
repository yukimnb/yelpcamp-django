from django.urls import path

from .views import DetailView, IndexView

app_name = "campgrounds"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:id>", DetailView.as_view(), name="show"),
]
