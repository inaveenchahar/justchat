from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ProfileModel


def sign_up(request):
    """

    :param request:
    :return: user account created and redirected to home page

    view to sign up users
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            new_user = User.objects.create_user(
                first_name=instance.first_name,
                last_name=instance.last_name,
                username=instance.username.lower(),
                email=instance.email,
                password=instance.password
            )
            new_profile = ProfileModel.objects.create(user=new_user)
            """
                try else is to send email
            """
            try:
                send_mail(
                    subject="Welcome",
                    recipient_list=new_user.email,
                    from_email=settings.EMAIL_HOST_USER,
                    fail_silently=True,
                    message="Your account has been created with us with username {name}\n"
                            "Thankyou😊".format(name=new_user.username)
                )
            except Exception as e:
                print(e)
            login(request, new_user)
            messages.success(request, 'You have successfully signed up as {name}.'.format(name=new_user.username))
            return redirect('main:home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def log_out(request):
    """
    :param request:
    :return: user logged out
    """
    if request.user.is_authenticated:
        logout(request)
        messages.error(request, 'You are logged out now.')
        return redirect('main:home')
    else:
        return redirect('main:home')


def login_view(request):
    """
    :param request:
    :return: user logged in

    normal user will be redirected to homepage and superuser to seller dashboard
    """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged as {name}.'.format(name=user.username))
            return redirect('main:home')
    else:
        form = LoginForm()
    return render(request, 'login_view.html', {'form': form})
