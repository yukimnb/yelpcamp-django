from django.contrib import admin

from .models import Campground, Review

# Register your models here.
admin.site.register(Campground)
admin.site.register(Review)
