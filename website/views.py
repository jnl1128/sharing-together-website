from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Chat
from django.views import View
from .forms import PostForm

# Create your views here.

#main view 관련
def main (request):
    return render(request, 'website/main.html', {})

#to_gather view 관련
def to_gather(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/to_gather.html', {'posts': posts})

def to_gather_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'website/to_gather_list.html', {'post': post})

def to_gather_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():    ## 잘못된 값이 저장되는 것을 방지하기 위해
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('to_gather_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'website/to_gather_edit.html', {'form': form}) # 새로운 글 만드는 view

def to_gather_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        form = PostForm(instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('to_gather_list', pk=post.pk)
        else:
            messages.error(request, "Error")
    else:
        form = PostForm(instance=post)
    return render(request, 'website/to_gather_edit.html', {'form': form})  # 글 수정하는 view

#be_together view 관련
def be_together(request):
    chats = Chat.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/be_together.html', {'chats': chats})

def be_together_list(request, pk):
    chat = get_object_or_404(Chat, pk = pk)
    return render(request, 'website/be_together_list.html', {'chat': chat})
