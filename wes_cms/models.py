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


class NavigationManager(models.Manager):
    def get_first(self):
        top_level_navs = self.filter(parent=None)
        if top_level_navs:
            return top_level_navs[0]

class Navigation(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    text = models.CharField(max_length=100)
    order = models.IntegerField()
    article = models.ForeignKey(Article, blank=True, null=True)

    objects = NavigationManager()

    def get_article(self):
        if self.article:
            return self.article
        else:
            for navigation in self.navigation_set.all():
                if navigation.article:
                    return navigation.article
                else:
                    return navigation.get_article()

    def __str__(self):
        return self.text

    def Meta(self):
        ordering = ['parent__order', 'order']