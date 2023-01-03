from django.contrib import admin

from authentication.models import User, Company, Branch
    
class User_admin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

class Company_admin(admin.ModelAdmin):
    list_display = ('name',)

class Branch_admin(admin.ModelAdmin):
    list_display = ('name', 'company')

admin.site.register(User, User_admin)
admin.site.register(Company, Company_admin)
admin.site.register(Branch, Branch_admin)