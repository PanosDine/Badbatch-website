from django.urls import path
from . import views



app_name="public"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('discography/', views.discography.as_view(), name="discography"),
    path('videos/', views.my_video, name="videos")
]