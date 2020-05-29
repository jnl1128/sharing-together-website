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
    return render(request, 'website/to_gather_list.html', {'post': post})

def to_gather_list_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('to_gather_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'website/to_gather_list_edit.html', {'form': form})

def to_gather_list_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('to_gather_list', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'website/to_gather_list_edit.html', {'form': form})
