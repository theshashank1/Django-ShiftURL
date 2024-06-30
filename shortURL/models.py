from django.db import models


class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_url} -> {self.original_url} -> {self.clicks} -> {self.created_at}"



# Create your models here.
