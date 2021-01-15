from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Room(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False, default=uuid.uuid4)
    room_members = models.ManyToManyField(User, related_name='RoomMembers')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) + ' -' + str(self.slug)


class ChatModel(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sent_by.username
