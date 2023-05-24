from django.contrib import admin

from blog.forms import AdminBlogPostForm
from blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    form = AdminBlogPostForm
    fieldsets = [
        ("About", {"fields": ["title", "publish_date", "category"]}),
        ("Content", {"fields": ["main_image", "content"]})
    ]
