# dodajemy brakujący import
from django.shortcuts import render
from .models import Category, Topic, Post

def category_list(request):
    # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
    categories = Category.objects.all()

    return render(request,
                  "posts/category/list.html",
                  {'categories': categories})

def category_detail(request, id):
    # pobieramy konkretny obiekt Category
    category = Category.objects.get(id=id)

    return render(request,
                  "posts/category/detail.html",
                  {'category': category})

def topic_list(request):
    # pobieramy wszystkie obiekty topic z bazy poprzez QuerySet
    topics = Topic.objects.all()

    return render(request,
                  "posts/topic/list.html",
                  {'topics': topics})

def topic_detail(request, name):
    # pobieramy konkretny obiekt topic
    topic = Topic.objects.get(name=name)

    return render(request,
                  "posts/topic/detail.html",
                  {'topic': topic})

from django.shortcuts import render, get_object_or_404
from .models import Topic, Post

def topic_detail_more(request, name):
    topic = get_object_or_404(Topic, name=name)

    posts = Post.objects.filter(topic=topic).order_by('-created_at')

    context = {
        'topic': topic,
        'posts': posts
    }

    return render(request, 'topic_detail_more.html', context)

def post_list(request):
    # pobieramy wszystkie obiekty post z bazy poprzez QuerySet
    posts = Post.objects.all()

    return render(request,
                  "posts/post/list.html",
                  {'posts': posts})

def post_detail(request, title):
    # pobieramy konkretny obiekt post
    post = Post.objects.get(title=title)

    return render(request,
                  "posts/post/detail.html",
                  {'post': post})