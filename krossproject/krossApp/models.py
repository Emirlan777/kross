from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField("заг", max_length=255)
    postDate = models.DateTimeField("дата и время", default=datetime.now)
    content = models.TextField("контент")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
