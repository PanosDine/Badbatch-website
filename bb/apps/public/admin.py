from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Video, Track

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'video']}),
    ]
    list_display = ('title', 'video')
    list_filter = ['title']
    search_fields = ['title']
    
admin.site.register(Video, VideoAdmin)

class TrackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'url']}),
    ]
    list_display = ('title', 'url')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Track, TrackAdmin)

