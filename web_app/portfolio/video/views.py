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


def video_category(request, Category):
    videos = Video.objects.filter(
        categories__name__contains=Category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": Category,
        "videos": videos
    }
    return render(request, "video_category.html", context)

