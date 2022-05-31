from django.conf import settings
from django.utils import timezone
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published = timezone.now()

    def __str__(self):
        return self.title
