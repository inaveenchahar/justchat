from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, ChatModel
from django.contrib.auth.models import User
# Create your views here.



# def index(request):
#
#     return render(request, 'index.html')


# # @login_required()
def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            room_name = request.POST.get('room-name-input')
            new_room = Room.objects.create(title=room_name, created_by=request.user)
            return redirect('room', new_room.slug)
        return render(request, 'index.html')
    else:
        return HttpResponse('Login required')


def inbox_conversation(request):
    all_conversations = Room.objects.filter(room_members__in=[request.user])
    return render(request, 'inbox_conversation.html', {'all_conversations': all_conversations})


def index_room(request, username):
    if request.user.is_authenticated:
        selected_user = User.objects.get(username=username)
        room_name = str(request.user.username) + '-AND-' + str(username)
        reverse_name = str(username) + '-AND-' + str(request.user.username)
        if Room.objects.filter(title__in=[room_name, reverse_name]).exists():
            room = Room.objects.get(title__in=[room_name, reverse_name])
            return redirect('room', room.slug)
        new_room = Room.objects.create(title=room_name,
                                       created_by=request.user)
        new_room.room_members.add(request.user, selected_user)
        new_room.save()
        return redirect('room', new_room.slug)
    return redirect('main:home')


def room_view(request, room_name):
    if request.user.is_authenticated:
        current_room = get_object_or_404(Room, slug=room_name)
        if request.user in current_room.room_members.all():
            # only last 50 messages will be visible in the room
            all_messages = ChatModel.objects.filter(room=current_room).order_by('added_on')[:50]
            return render(request, 'room.html', {'room_name': room_name,
                                                 'current_room': current_room,
                                                 'all_messages': all_messages
                                                 })
        return redirect('main:home')
    else:
        return HttpResponse('Login required')
