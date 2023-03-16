from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/:id', views.room, name="room")
]
