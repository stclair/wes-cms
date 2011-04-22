
from google.appengine.api import images
from django.db import models

class BaseImageModel(models.Model):
    full_size_image = models.FileField(verbose_name="Image", upload_to='images/')
    serving_url = models.URLField(blank=True)

    class Meta(object):
        abstract = True

    def _get_blobstore_key(self):
        return str(self.full_size_image.file.blobstore_info.key())

    def get_sized_image(self, size=None):
        serving_url = self.serving_url
        if size:
            serving_url += '=s%s' % size
        return serving_url

    def get_image_name(self):
        return self.full_size_image.file.blobstore_info.filename

    def save(self, force_insert=False, force_update=False, using=None):
        """
        saves the serving url so we never need an rpc to generate it.
        """
        self.serving_url = images.get_serving_url(self._get_blobstore_key())
        return super(BaseImageModel, self).save(force_insert, force_update, using)

