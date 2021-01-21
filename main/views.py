from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import ProfileModel

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def home(request):
    all_user = ProfileModel.objects.all().exclude(user=request.user).order_by('-user__last_login')
    paginator = Paginator(all_user, 24)  # Show 24 users per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


def profile_detail(request, username):
    selected_user = get_object_or_404(User, username=username)
    profile = get_object_or_404(ProfileModel, user=selected_user)
    return render(request, 'profile_detail.html', {'profile': profile})
