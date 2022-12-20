from django.contrib import admin

from authentication.models import User
    
class User_admin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

admin.site.register(User, User_admin)
