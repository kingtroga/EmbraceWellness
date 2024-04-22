from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from . import models
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ForumForm

def index(request):
    query = request.GET.get('query', '')
    forums = models.Forum.objects.all()

    if query:
        forums = forums.filter(Q(title__icontains=query) | Q(content__icontains=query))


    paginator = Paginator(forums, 6) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # clean up forum
    for forum in page_obj:
        forum.content = forum.content[0:500] + "..."

    return render(request, 'forum/forum_index.html',
                  {"forums": forums,
                   'query': query,
                   "page_obj": page_obj})


@login_required
def new(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            new_forum = form.save(commit=False)
            new_forum.created_by = request.user
            new_forum.save()
            return redirect("forum:index") #TODO: Redirect to the forum post detail
    else:
        form = ForumForm()
    return render(request, 'forum/forum_new.html',{
        "form": form
    })


def detail(request, pk):
    forum = get_object_or_404(models.Forum, pk=pk)
    
    return render(request, 'forum/detail.html', {
        "forum": forum
    })


