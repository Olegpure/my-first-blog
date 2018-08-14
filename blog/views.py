from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# Create your views here.
# A view is a place where we put the "logic" of our application. It will request information from the model you created before and pass it to a template

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# As you can see, we created a function (def) called post_list that takes request and return a function render that will render (put together) our template blog/post_list.html.