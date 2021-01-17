from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.inbox_conversation, name='inbox'),
    path('connect/<username>/', views.index_room, name='index_room'),
    path('<room_name>/', views.room_view, name='room')
]
