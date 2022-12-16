from django.contrib import admin
from .models import All_Post, Following_Follower, following_system, liked_system

# Register your models here.
admin.site.register(All_Post)
admin.site.register(Following_Follower)
admin.site.register(following_system)
admin.site.register(liked_system)

