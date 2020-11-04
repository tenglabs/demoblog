from django.contrib import admin

from .models import Post, Comment #model import from local file (blog/models.py)

# Register your models here.
admin.site.register(Post) #adding our model to admin page

@admin.register(Comment)#Making custom comments admin page
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','text')