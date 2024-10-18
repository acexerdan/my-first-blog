from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # defines model/object, Post: name of model, Post is a models.Model, so Django knows that it should be saved in DB
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # a link to another model
    title = models.CharField(max_length=200) # text with a limited number of characters
    text = models.TextField() #  long text without a limit
    created_date = models.DateTimeField(default=timezone.now) # date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title