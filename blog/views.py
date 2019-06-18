
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    me = User.objects.get(username='ebaeyens')
    posts = Post.objects.filter(author=me).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


