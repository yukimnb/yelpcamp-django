from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import CreateForm
from .models import Campground


class ListCampground(generic.ListView):
    model = Campground
    template_name = "list.html"
    context_object_name = "campgrounds"


class DetailCampground(generic.DetailView):
    model = Campground
    template_name = "detail.html"
    context_object_name = "campground"
    pk_url_kwarg = "id"


class CreateCampground(generic.CreateView):
    model = Campground
    template_name = "create.html"
    form_class = CreateForm
    success_url = reverse_lazy("campgrounds:list")

    def form_valid(self, form):
        messages.success(self.request, "キャンプ場を作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "キャンプ場の作成に失敗しました")
        return super().form_invalid(form)
