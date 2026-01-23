from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch the post or show 404
    return render(request, 'blog/post_detail.html', {'post': post})
