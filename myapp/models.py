from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.utils.text import slugify
from autoslug import AutoSlugField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    read_min = models.IntegerField(default=2)
    author = models.ForeignKey(User, related_name='myapp_posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
