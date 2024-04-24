from django.shortcuts import render
from .models import Contact

def index(request):
    user_is_staff = request.user.is_staff
    direct_messages = Contact.objects.all()


    for direct_message in direct_messages:
        direct_message.subject = direct_message.subject[0:50] + "..."

    return render(request, 'contact/contact_index.html', {
        'user_is_staff': user_is_staff,
        'direct_messages': direct_messages,
    })