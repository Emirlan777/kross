from django.shortcuts import render, get_object_or_404
from .models import Post

def homePage(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "home.html", {
        'posts': posts
    })


def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post-detail.html", {
       'post': post
    })