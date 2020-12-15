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
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
        
class Like(models.Model):
    liked_user = models.ForeignKey(User, related_name='liked_users', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, related_name='liked_posts', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return ('%s LIKED -  %s' % (self.liked_user, self.post))

class Dislike(models.Model):
    disliked_user = models.ForeignKey(User, related_name='disliked_users', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_disliked = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return ('%s DISLIKED -  %s' % (self.disliked_user, self.post))


