from synat_help.help_example.models import Article, Category
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
