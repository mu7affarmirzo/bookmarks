from django.contrib import admin
from .models import ImageModel

@admin.register(ImageModel)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
