from django.shortcuts import render
from .models import Contact

def index(request):
    user_is_staff = request.user.is_staff
    return render(request, 'contact/contact_index.html', {
        'user_is_staff': user_is_staff
    })