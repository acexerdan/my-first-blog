from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# takes request and will return the value it gets from calling render that will render 
# (put together) the template blog/post_list.html.
# Params:
# request: everything we receive from the user via the Internet
# 'blog/post_list.html': template file 
# {'posts': posts}: things for the template to use