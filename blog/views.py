from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# takes request and will return the value it gets from calling render that will render 
# (put together) the template blog/post_list.html.
# Params:
# request: everything we receive from the user via the Internet
# 'blog/post_list.html': template file 
# {'posts': posts}: things for the template to use

# get_object_or_404:  In case there is no Post with the given pk, it will display much nicer page,
# the Page Not Found 404 page.

# All the fields from the form are in request.POST
# Need to handle 2 situations: 1) when we access the page for the first time and we want a blank form,
# 2) when we go back to the view with all form data we just typed to construct the PostForm with data from the form
# Also, check if the form is correct (all required fields are set and no incorrect values submitted) with form.is_valid().
# If form is valid, then save it with form.save (commit=False means don't save the Post model yet) and add an author 
# post.save() will preserve changes (adding the author) and a new blog post is created
# To immediately go to the post_detail page for any newly created blog post, use return redirect('post_detail', pk=post.pk)

# For the form, we get the Post model we want to edit with get_object_or_404(Post, pk=pk), then when
# we create a form, we pass this post as an instance, both when we save the form and and when we have just opened a form with this post to edit

