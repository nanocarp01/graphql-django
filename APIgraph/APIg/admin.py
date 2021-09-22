from django.contrib import admin
from .models import API
# Register your models here.

class search(admin.ModelAdmin):
    list_display = ('legajo', "agente")
    search_fields = ('legajo', 'secretaria')



admin.site.register(API, search)
