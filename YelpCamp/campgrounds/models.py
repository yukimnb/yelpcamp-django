from django.db import models


class Campground(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    price = models.PositiveIntegerField(verbose_name="価格")
    location = models.CharField(max_length=100, verbose_name="場所")
    description = models.TextField(verbose_name="説明")
    image = models.URLField(null=True, blank=True, verbose_name="画像URL")

    class Meta:
        verbose_name_plural = "Campground"

    def __str__(self):
        return self.title


class Review(models.Model):
    campground = models.ForeignKey(Campground, on_delete=models.CASCADE, verbose_name="キャンプ場")
    comment = models.TextField(verbose_name="コメント")
    rating = models.CharField(verbose_name="レーティング", max_length=10)

    class Meta:
        verbose_name_plural = "Review"
