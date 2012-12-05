from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    long_description = models.TextField()
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title


