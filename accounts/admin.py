from django.contrib import admin
from .models import ProfileModel

# Register your models here.


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'added_on', 'updated_on']
    search_fields = ['user__username']
    list_per_page = 20
    list_filter = ['gender']
