from django.views import generic

from .models import Campground


class IndexView(generic.ListView):
    model = Campground
    template_name = "index.html"
    context_object_name = "campgrounds"
