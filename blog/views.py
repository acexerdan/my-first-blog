from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

# takes request and will return the value it gets from calling render that will render 
# (put together) the template blog/post_list.html.