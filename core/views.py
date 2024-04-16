from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout

def index(request):
    return render(request, "core\index.html")

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

