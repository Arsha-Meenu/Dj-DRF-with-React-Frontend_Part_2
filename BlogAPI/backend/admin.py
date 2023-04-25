from django.contrib import admin
from .models import Articles


# admin.site.register(Articles)
@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','published')
    date_hierarchy = ('published')
    search_fields = ['title']
