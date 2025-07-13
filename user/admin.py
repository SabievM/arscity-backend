from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')




from django.contrib import admin

admin.site.site_header = "Админ панель сайта ars-city.ru"
admin.site.site_title = "Название вкладки браузера" 
admin.site.index_title = "Добро пожаловать в админку" 
admin.site.site_url = "https://ars-city.ru"