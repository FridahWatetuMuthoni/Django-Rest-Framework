from django.contrib import admin
from .models import Tag, User, Post

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Post)
