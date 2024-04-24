from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from forum.models import Forum
from blog.models import Blog
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm


def detail(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    forums = Forum.objects.filter(created_by=user).all()[0:3]
    blogs = Blog.objects.filter(author=user).all()[0:3]
    user_is_staff = request.user.is_staff

    return render(request, 'accounts/detail.html', {
        'profile': profile,
        'forums': forums,
        'blogs': blogs,
        'user_is_staff': user_is_staff
    } )

@login_required
def edit_profile_pic(request, pk):
    user_is_staff = request.user.is_staff
    profile = get_object_or_404(Profile, pk=pk)
    
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form
            return redirect(f'/profile/{profile.user.username}/')
    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile_pic.html', {
        'profile_form': profile_form,
        'user_is_staff': user_is_staff
    })

@login_required  
def edit_profile_text(request, pk):
    user_is_staff = request.user.is_staff
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save(commit=True)
            return redirect(f'/profile/{user.username}/')
    else:
        user_form = UserForm(instance=user)

    return render(request, 'accounts/edit_profile_text.html', {
        'user_form': user_form,
        'user_is_staff': user_is_staff
    } )

def professionals(request):
    user_is_staff = request.user.is_staff
    
    return render(request, 'accounts/professionals.html', {
        'user_is_staff': user_is_staff,
    })