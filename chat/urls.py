from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('connect/<username>/', views.index_room, name='index_room'),
    path('<room_name>/', views.room_view, name='room')
]
