from django.shortcuts import render, get_object_or_404
from .models import Contact

def index(request):
    user_is_staff = request.user.is_staff
    direct_messages = Contact.objects.filter(attended_to=False).all()


    for direct_message in direct_messages:
        direct_message.subject = direct_message.subject[0:50] + "..."

    return render(request, 'contact/contact_index.html', {
        'user_is_staff': user_is_staff,
        'direct_messages': direct_messages,
    })

def detail(request, pk):
    message = get_object_or_404(Contact, pk=pk)
    user_is_staff = request.user.is_staff

    return render(request, 'contact/detail.html', {
        'user_is_staff': user_is_staff,
        'message': message,
    })

