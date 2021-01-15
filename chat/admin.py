from django.contrib import admin
from .models import Room, ChatModel
# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_by', 'added_on', 'updated_on']


@admin.register(ChatModel)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['room', 'sent_by', 'added_on', 'updated_on']
