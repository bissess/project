from django.contrib import admin

from .models import PostCategory, Post, Comment


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'image', 'slug', 'category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['text']