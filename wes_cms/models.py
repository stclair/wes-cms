from django.db import models

from images.models import BaseImageModel

class Article(models.Model):
    slug = models.SlugField()
    text = models.TextField()

    def get_url(self):
        return "/%s/" % self.slug

    def __str__(self):
        return self.slug

class Image(BaseImageModel):
    description = models.CharField(max_length=1000)

    def get_sample_url(self):
        return self.get_sized_image(200)

    def __str__(self):
        return "%s (%s)" % (self. description, self.get_sized_image(100))

class NavigationHeaderManager(models.Manager):
    def get_first(self):
        return self.all()[0]

class NavigationHeader(models.Model):
    text = models.CharField(max_length=100)
    order = models.IntegerField()

    objects = NavigationHeaderManager()    

    def __str__(self):
        return self.text

    def Meta(self):
        ordering = ['order']

class NavigationManager(models.Manager):
    def get_first(self):
        header = NavigationHeader.objects.get_first()
        return self.filter(header=header)[0]

class Navigation(models.Model):
    header = models.ForeignKey(NavigationHeader)
    text = models.CharField(max_length=100)
    order = models.IntegerField()
    article = models.ForeignKey(Article)

    objects = NavigationManager()

    def __str__(self):
        return self.text

    def Meta(self):
        ordering = ['header__order', 'order']