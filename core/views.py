from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout
from forum.models import Forum
from blog.models import Blog
from contact.forms import ContactForm



def index(request):
    forums = Forum.objects.all()[0:3]
    blogs = Blog.objects.all()[0:3]
    user_is_staff = request.user.is_staff

    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("core:index")
        
    else:
        form = ContactForm()
    
    # clean up forum
    for forum in forums:
        forum.content = forum.content[0:500] + "..."

    return render(request, "core\index.html", {
        "forums": forums,
        "blogs": blogs,
        "form": form,
        "user_is_staff": user_is_staff,
    })

def signup(request):
    user_is_staff = request.user.is_staff
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            signup_form = signup_form.save(commit=True)
            return redirect('/login/')
        
    else:
        signup_form = SignUpForm()


    return render(request, 'core\signup.html', {
        'signup_form': signup_form,
        'user_is_staff': user_is_staff
    })

def logout_view(request):
    logout(request)
    return redirect('/')

