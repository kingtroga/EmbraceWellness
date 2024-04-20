from django.shortcuts import render
from django.db.models import Q
from . import models

def index(request):
    query = request.GET.get('query', '')
    forums = models.Forum.objects.all()

    if query:
        forums = forums.filter(Q(title__icontains=query) | Q(content__icontains=query))
        

    return render(request, 'forum/forum_index.html',
                  {"forums": forums,
                   'query': query,})


