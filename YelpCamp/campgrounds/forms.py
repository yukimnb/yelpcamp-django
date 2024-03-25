from django.forms import ModelForm

from .models import Campground


class CreateForm(ModelForm):
    class Meta:
        model = Campground
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
