from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from django.contrib.auth.models import User
from accounts.models import ProfileModel

from django.core.paginator import Paginator
# Create your views here.


def home(request):
    all_user = ProfileModel.objects.all().order_by('-user__last_login')
    if request.user.is_authenticated:
        all_user = all_user.exclude(user=request.user)
    all_ages = [i for i in range(16, 101)]

    # search users by their username
    username_query = request.GET.get('q')
    if username_query:
        all_user = ProfileModel.objects.filter(user__username__icontains=username_query).exclude(user=request.user).order_by('-user__last_login')

    # filter user by age and gender
    age_query = request.GET.get('aFilter')
    gender_query = request.GET.get('gender')
    excluded_query = ['All', 'None', None]
    try:
        if age_query in all_ages and gender_query not in excluded_query:
            all_user = ProfileModel.objects.filter(age=age_query, gender=gender_query).exclude(user=request.user).order_by('-user__last_login')
        elif age_query in all_ages:
            all_user = ProfileModel.objects.filter(age=age_query).exclude(user=request.user).order_by('-user__last_login')
        elif gender_query and gender_query not in excluded_query:
            all_user = ProfileModel.objects.filter(gender=gender_query).exclude(user=request.user).order_by('-user__last_login')
    except Exception as e:
        print(e)
        return redirect('main:home')

    # pagination
    paginator = Paginator(all_user, 24)  # Show 24 users per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj, 'all_ages': all_ages})


def profile_detail(request, username):
    selected_user = get_object_or_404(User, username=username)
    profile = get_object_or_404(ProfileModel, user=selected_user)
    return render(request, 'profile_detail.html', {'profile': profile})
