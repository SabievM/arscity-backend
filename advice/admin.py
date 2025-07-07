from django.contrib import admin
from .models import Advice

@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'description')