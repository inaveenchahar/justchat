# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import ChatModel, Room
from django.utils.timezone import datetime


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        room_slug = self.scope['url_route']['kwargs']['room_name']
        current_room = Room.objects.get(slug=room_slug)
        new_message = ChatModel.objects.create(sent_by=self.scope['user'], message=message, room=current_room)
        current_room.last_text_send_at = datetime.now()
        current_room.save()

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        # gets the most recent message from the room by filtering room slug
        room_slug = self.scope['url_route']['kwargs']['room_name']
        current_room = Room.objects.get(slug=room_slug)
        last_message = ChatModel.objects.filter(room=current_room).first()

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': last_message.message,
            'sent_by': last_message.sent_by.username,
        }))
