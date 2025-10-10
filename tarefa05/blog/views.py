from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, id):
    postagem = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post.html', {'post': postagem})

