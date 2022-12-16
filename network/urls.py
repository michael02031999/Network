
from django.urls import path

from . import views

urlpatterns = [
    path("following", views.following, name="following"),
    path("profile_page/<str:username>/", views.profile_page, name="profile_page"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #API Routes
    path("change_likes/<int:id>/<str:like_or_dislike>", views.change_likes, name="change_likes"),
    path("comment/<int:id>/<str:comment>", views.change_comment, name="change_comment")
]
