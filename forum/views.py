from django.shortcuts import render, redirect
from django.utils import timezone
from POSTS.models import Post
from django.shortcuts import render, get_object_or_404
from POSTS.form import PostForm


def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post_list.html')

def post(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post.html', {'posts': post})

def post_detail(request, pk  ):
    post = [get_object_or_404(Post, pk=pk), Post.objects.get(pk= pk)]
    return render(request, 'forum/post_detail.html',  {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})