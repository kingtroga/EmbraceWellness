from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout
from forum.models import Forum
from blog.models import Blog



def index(request):
    forums = Forum.objects.all()[0:3]
    blogs = Blog.objects.all()[0:3]
    
    # clean up forum
    for forum in forums:
        forum.content = forum.content[0:500] + "..."

    return render(request, "core\index.html", {
        "forums": forums,
        "blogs": blogs,
    })

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form = form.save(commit=True)
            return redirect('/login/')
        
    else:
        form = SignUpForm()


    return render(request, 'core\signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('/')

