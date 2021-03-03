from django.shortcuts import render,redirect
from .models import Video, Category

def home(request):
    return redirect('/videos/')

def video_index(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, "video_index.html", context)

def video_detail(request, id):
    video = Video.objects.get(id=id)
    context = {
        "video": video,
    }

    return render(request, "video_detail.html", context)

def blog_category(request, category):
    videos = Video.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "videos": videos
    }
    return render(request, "video_category.html", context)

