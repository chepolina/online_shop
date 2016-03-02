from django.db import models
from django.utils import timezone
# from django.db import models
#
# class CategoryField(ListField):
#     def formfield(self, **kwargs):
#         return models.Field.formfield(self, StringListField, **kwargs)
#
# class Post(models.Model):
#     title = models.CharField(max_length=100)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.TextField()
    cost = models.IntegerField()
    weight = models.FloatField(0.0)
    image = models.ImageField(upload_to="%Y/%m/%d/", height_field=None, width_field=None, max_length=100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title