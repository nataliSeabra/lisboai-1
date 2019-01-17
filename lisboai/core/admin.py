from django.contrib import admin
from lisboai.core.models import Categories,Article,Social


# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    fields = ('name', 'active')
    list_display = ('name', 'active')
admin.site.register(Categories, CategoriesAdmin)


class ArticleAdmin(admin.ModelAdmin):

    fields = ('categories', 'short_description', 'description','state')
    list_display = ('categories', 'short_description','state')
admin.site.register(Article, ArticleAdmin)


class SocialAdmin(admin.ModelAdmin):
    fields = ('name', 'link')
    list_display = ('name', 'link')
admin.site.register(Social, SocialAdmin)