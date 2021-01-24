from django.contrib import admin
from django.urls import path, include

from . import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bb.apps.public.urls')),
]
