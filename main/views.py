from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import ProfileModel
# Create your views here.


def home(request):
    all_user = ProfileModel.objects.all().exclude(user__username=request.user.username)
        # .exclude(username=request.user.username)
    return render(request, 'home.html', {'all_user': all_user})


def profile_detail(request, username):
    selected_user = get_object_or_404(User, username=username)
    profile = get_object_or_404(ProfileModel, user=selected_user)
    return render(request, 'profile_detail.html', {'profile': profile})
