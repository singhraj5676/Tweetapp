from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile,Meep
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]


admin.site.unregister(User)

admin.site.register(User, UserAmin)

admin.site.register(Profile)

class Profileline(admin.StackedInline):
    model = Profile

admin.site.register(Meep)