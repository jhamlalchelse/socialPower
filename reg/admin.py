from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PostDetail)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','post_image','desc','user','uploaded_at']

@admin.register(MessageModel)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','user','comment','postid']

@admin.register(FollowerModel)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','user','fweruserid']

@admin.register(FollowingModel)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','user','fwinguserid']