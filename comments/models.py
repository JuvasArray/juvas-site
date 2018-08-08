from django.db import models
from django.conf import settings

# Create your models here.

from posts.models import Post

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
