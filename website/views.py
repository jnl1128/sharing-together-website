from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.views import View
from .forms import PostForm

# Create your views here.

def to_gather(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/to_gather.html', {'posts': posts})

def to_gather_list(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'website/post_detail.html', {'post': post})

def main (request):
    return render(request, 'website/main.html', {})
