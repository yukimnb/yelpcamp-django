from django.db import models


class Campground(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Campground"

    def __str__(self):
        return self.title
