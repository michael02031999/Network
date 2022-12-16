from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import User, All_Post, Following_Follower, following_system, liked_system


from datetime import date
from datetime import datetime
from pytz import timezone

tz = timezone('EST')

def change_likes(request, id, like_or_dislike):

    if like_or_dislike == "like":

        liked_system.objects.create(liker = request.user, receiverId = id)

        All_likes = liked_system.objects.all().filter(liker = request.user)

        list_of_ids = []

        for like in All_likes:
            list_of_ids.append(like.receiverId)

        count = All_Post.objects.filter(id=id)

        print(count[0].likes)

        newCount = int(count[0].likes) + 1

        count.update(likes = newCount)


    else:

        print("dislike was pressed")
        liked_system.objects.filter(receiverId=id).delete()

        All_likes = liked_system.objects.all().filter(liker = request.user)

        list_of_ids = []

        for like in All_likes:
            list_of_ids.append(like.receiverId)

        count = All_Post.objects.filter(id=id)

        print(count[0].likes)

        newCount = int(count[0].likes) - 1

        count.update(likes = newCount)

        


    
    All_Posts = All_Post.objects.all().order_by('datetime').reverse()

    post_paginator = Paginator(All_Posts, 10)

    page_num = request.GET.get('page')

    page = post_paginator.get_page(page_num)

    return render(request, "network/index.html", {
        "All_Posts": post_paginator.object_list,
        "page": page,
        "ids": list_of_ids
    })
    

    



def change_comment(request, id, comment):

    edit = All_Post.objects.filter(id=id)

    edit.update(comment = comment)

    All_Posts = All_Post.objects.all().order_by('datetime').reverse()

    post_paginator = Paginator(All_Posts, 10)

    page_num = request.GET.get('page')

    page = post_paginator.get_page(page_num)

    return render(request, "network/index.html", {
        "All_Posts": post_paginator.object_list,
        "page": page
    })

def following(request):
    following_list = following_system.objects.filter(follower=request.user)
    posts_you_follow = []
    leaders = []

    for people in following_list:
        leaders.append(people.leader)

    listofquerysets = []

    for leader in leaders:
        posts = All_Post.objects.filter(username = leader).order_by('datetime').reverse()
        for post in posts:
            listofquerysets.append(post)
    
    querySetlist = []

    for querySet in listofquerysets:
        timestamp=str(querySet.datetime)
        querySetTuple = (querySet, timestamp[:19])

        querySetlist.append(querySetTuple)

    sorted_list = sorted(querySetlist, key=lambda t: datetime.strptime(t[1], '%Y-%m-%d %H:%M:%S'))

    All_Posts = []

    for tuple in sorted_list:
        entry = list(tuple)
        All_Posts.append(entry[0])

    All_Posts.reverse()

    for post in All_Posts:
        posts_you_follow.append(post)

    
    follow_paginator = Paginator(posts_you_follow, 10)

    page_num = request.GET.get('page')

    page = follow_paginator.get_page(page_num)

    All_likes = liked_system.objects.all().filter(liker = request.user)

    list_of_ids = []

    for like in All_likes:
        list_of_ids.append(like.receiverId)

    return render(request, "network/following.html", {
        "followed_posts": posts_you_follow,
        "page": page,
        "ids": list_of_ids
    })

def profile_page(request, username):

    user = Following_Follower.objects.filter(username = username)
    posts_from_user = All_Post.objects.filter(username = username).order_by('datetime').reverse()
    following_list = following_system.objects.filter(follower = request.user, leader = username)

    if (following_list.count() == 0):
        message = "Follow"
    else: 
        message = "Unfollow"

    print(user)
    profile = {
        "username": user[0].username,
        "following": user[0].following, 
        "followers": user[0].followers, 
        "posts_from_user": posts_from_user,
        "message": message 
    }

    if request.method == "POST":

        follow = request.POST.get("follow")

        if (follow == "Follow"):
            new_follower=following_system(follower=request.user, leader = username)
            new_follower.save()
            follow = "Unfollow"
        
        else:
            oneless_follower = following_system.objects.filter(follower=request.user, leader = username)
            oneless_follower.delete()
            follow = "Follow"
        
        profile["message"] = follow

        return render(request, "network/profile_page.html", profile)

    return render(request, "network/profile_page.html", profile)

def index(request):
    if request.method == "POST":
        now = datetime.now(tz)
        post = {
            "username": request.POST.get("username"),
            "comment": request.POST.get("post_comment"),
            "date": date.today(),
            "time": now.strftime("%H:%M:%S"),
            "number_of_likes": 0
        }

        #Test out the new date !!
        
        All_Post.objects.create(username = request.POST.get('username'), comment = request.POST.get('post_comment'),
        date = now.strftime("%B %d, %Y"), time = now.strftime("%I:%M %p"), likes = 0)

        All_Posts = All_Post.objects.all().order_by('datetime').reverse()

        post_paginator = Paginator(All_Posts, 10)

        page = post_paginator.get_page(1)

        return render(request, "network/index.html", {
            "All_Posts": All_Posts,
            "page": page,
        })

    All_Posts = All_Post.objects.all().order_by('datetime').reverse()

    post_paginator = Paginator(All_Posts, 10)

    page_num = request.GET.get('page')

    page = post_paginator.get_page(page_num)

    All_likes = liked_system.objects.all().filter(liker = request.user)

    list_of_ids = []

    for like in All_likes:
        list_of_ids.append(like.receiverId)


    return render(request, "network/index.html", {
        "All_Posts": post_paginator.object_list,
        "page": page,
        "ids": list_of_ids
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user_follow=Following_Follower(username = username, following = 0, followers = 0)
            user.save()
            user_follow.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
