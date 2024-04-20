from django.shortcuts import render
from django.db.models import Q
from . import models
from django.core.paginator import Paginator

def index(request):
    query = request.GET.get('query', '')
    forums = models.Forum.objects.all()

    if query:
        forums = forums.filter(Q(title__icontains=query) | Q(content__icontains=query))


    paginator = Paginator(forums, 6) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
        

    return render(request, 'forum/forum_index.html',
                  {"forums": forums,
                   'query': query,
                   "page_obj": page_obj})


