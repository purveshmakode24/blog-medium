from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.utils.text import slugify
from autoslug import AutoSlugField
from hitcount.models import HitCount, HitCountMixin


class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', null=True)
    content = models.TextField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    date_posted = models.DateTimeField(default=timezone.now)
    read_min = models.IntegerField(default=2)
    author = models.ForeignKey(User, related_name='myapp_posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def _get_unique_slug(self):
    #     slug = slugify(self.title)
    #     unique_slug = slug
    #     num = 1
    #     while Post.objects.filter(slug=unique_slug).exists():
    #         unique_slug = '{}-{}'.format(slug, num)
    #         num += 1
    #     return unique_slug
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self._get_unique_slug()
    #     super().save(*args, **kwargs)
