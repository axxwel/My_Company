from django.contrib import admin

from authentication.models import User, Branch, Process
    
class User_admin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

class Branch_admin(admin.ModelAdmin):
    list_display = ('name',)

class Process_admin(admin.ModelAdmin):
    list_display = ('name', 'Branch')

admin.site.register(User, User_admin)
admin.site.register(Branch, Branch_admin)
admin.site.register(Process, Process_admin)