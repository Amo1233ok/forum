from django.shortcuts import render
from django.utils import timezone
from POSTS.models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post_list.html')

def post(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post.html', {'posts': post})

def post_detail(request, pk  ):
    post = [get_object_or_404(Post, pk=pk), Post.objects.get(pk= pk)]
    return render(request, 'forum/post_detail.html',  {'post': post})
