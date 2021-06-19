from django.contrib import admin
from django.contrib.auth.models import Group
from app_users.models import UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.unregister(Group)