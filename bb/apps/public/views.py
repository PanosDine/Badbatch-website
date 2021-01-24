from .models import Video, Track
from django.views import generic

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

"""simple views, no real functionality here, just rendering the 
corresponding templates"""
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

"""def discography(request: HttpRequest) -> HttpResponse:
    tracks = Track.objects.all().order_by('-id')
    return render(request, 'discography.html', {'tracks':tracks})"""

def my_video(request):
    obj=Video.objects.all().order_by('-id')
    return render(request, 'videos.html', {'obj':obj})


"""class VideoView(generic.ListView):
    model = Video
    context_object_name = 'videos'
    template_name = '../templates/videos.html'"""

class discography(generic.ListView):
    model = Track
    context_object_name = 'tracks'
    template_name = '../templates/discography.html'