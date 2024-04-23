from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from forum.models import Forum
from blog.models import Blog
from django.contrib.auth.decorators import login_required


def detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    forums = Forum.objects.filter(created_by=user).all()[0:3]
    blogs = Blog.objects.filter(author=user).all()[0:3]

    return render(request, 'accounts/detail.html', {
        'profile': profile,
        'forums': forums,
        'blogs': blogs
    } )

def edit(request, pk):
    pass
    