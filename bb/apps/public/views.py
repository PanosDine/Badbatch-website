from .models import Video, Track
from django.views import generic

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

"""simple views, no real functionality here, just rendering the 
corresponding templates"""

def index(request: HttpRequest) -> HttpResponse:
    latest_video = Video.objects.all().latest('id')
    return render(request, 'index.html', {'obj':latest_video})

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def my_video(request):
    obj=Video.objects.all().order_by('-id')
    return render(request, 'videos.html', {'obj':obj})

class discography(generic.ListView):
    model = Track
    context_object_name = 'tracks'
    template_name = '../templates/discography.html'