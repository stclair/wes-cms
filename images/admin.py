
from django.contrib import admin
from filetransfers.admin import FiletransferAdmin

class ImageAdminMixin(object):
    add_form_template = "images/change_form.html"
    change_form_template = "images/change_form.html"

    def listview_thumbnail(self, obj):
        return "<img src='%s' alt='image thumnail' />" % obj.get_sized_image(100)
    listview_thumbnail.allow_tags = True

    def image_name(self, obj):
        return obj.get_image_name()

class BaseImageAdmin(ImageAdminMixin, FiletransferAdmin):
    pass


#Sample Image Admin:
#
#class ImageAdmin(BaseImageAdmin):
#    list_display = ('listview_thumbnail', 'title', 'image_name', )
#    exclude = ('serving_url',)