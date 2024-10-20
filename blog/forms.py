from django import forms

from .models import Post

# PostForm is name of form, which is a ModelForm
# class Meta: tells Django the model to use to create this form (model = Post)
# then define the field(s) that should be in the form

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')