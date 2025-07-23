from django.shortcuts import render
from django.utils import timezone
from POSTS.models import Post

def post_list(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post_list.html')

def post(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post.html', {'posts': post})
