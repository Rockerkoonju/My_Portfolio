from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("videos/", views.video_index, name="video_index"),
    path("videos/<int:id>/", views.video_detail, name="video_detail"),
]
