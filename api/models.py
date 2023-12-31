from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
