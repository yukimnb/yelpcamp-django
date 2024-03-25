from django.views import generic

from .models import Campground


class IndexView(generic.ListView):
    model = Campground
    template_name = "index.html"
    context_object_name = "campgrounds"


class DetailView(generic.DetailView):
    model = Campground
    template_name = "show.html"
    context_object_name = "campground"
    pk_url_kwarg = "id"
