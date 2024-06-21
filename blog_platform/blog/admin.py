from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'title_tag')  
    list_filter = ('author',)  
    search_fields = ['title', 'author__username']  
admin.site.register(Post, PostAdmin)
