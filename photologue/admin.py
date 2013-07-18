""" Newforms Admin configuration for Photologue

"""
from django.contrib import admin
from models import *



class PhotoSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'height', 'crop', 'pre_cache')
    fieldsets = (
        (None, {
            'fields': ('name', 'width', 'height', 'quality')
        }),
        ('Options', {
            'fields': ('upscale', 'crop', 'pre_cache')
        }),
    )

admin.site.register(PhotoSize, PhotoSizeAdmin)
