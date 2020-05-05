from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'is_published', 'article', 'title', 'publish_date')
    list_display_links = ('author', 'article')
    list_editable = ("is_published",)
    search_fields = ('author', 'publish_date')
    list_per_page = 3
    list_filter = ('author', 'publish_date')

admin.site.register(Blog, BlogAdmin)


