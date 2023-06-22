from django.contrib import admin
from ads.models import Ads, Category


class AdsAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ads, AdsAdmin)
admin.site.register(Category, CategoryAdmin)