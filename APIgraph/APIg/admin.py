from django.contrib import admin
from .models import API
# Register your models here.

class search(admin.ModelAdmin):
    list_display = ('title', 'desc')
    search_fields = ('title', 'desc')



admin.site.register(API, search)
