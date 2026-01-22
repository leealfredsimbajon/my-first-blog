from django.shortcuts import render
from django.utils import timezone
from .models import Post   # import your Post model here, at the top

def post_list(request):
    # Get all published posts, ordered by published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # Pass the posts QuerySet to the template
    return render(request, 'blog/post_list.html', {'posts': posts})
