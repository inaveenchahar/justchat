from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import ProfileModel


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'style': 'font-size:14px;',
    }), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'style': 'font-size:14px;',
    }), label='Last Name')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'style': 'font-size:14px;',
    }), label='Username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'style': 'font-size:14px;',
    }), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'style': 'font-size:14px;',
    }), label='Password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'style': 'font-size:14px',
    }), label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'style': 'font-size:14px',
    }), label='Password', required=True)


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'style': 'font-size:14px;',
    }), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'style': 'font-size:14px;',
    }), label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    AGE = [(i, i) for i in range(16, 101)]
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={
        'class': 'form-control',
    }), label='Gender')
    age = forms.ChoiceField(choices=AGE, widget=forms.Select(attrs={
        'class': 'form-control',
    }), label='Age')
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'class': 'form-control',
        'placeholder': 'Bio',
        'style': 'font-size:14px;',
    }), label='Bio', required=False)

    class Meta:
        model = ProfileModel
        fields = ['profile_pic', 'age', 'gender', 'bio']

