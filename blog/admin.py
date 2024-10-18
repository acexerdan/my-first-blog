# To add, edit and delete the posts we've just modeled, we will use Django admin.
from django.contrib import admin
from .models import Post

admin.site.register(Post) # need to register the model to make the model visible on the admin page

# login page on http://127.0.0.1:8000/admin/