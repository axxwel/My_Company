from django.contrib import admin

from purchases_auth.models import Auth_datas
from purchases_auth.models import Auth_users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('login', 'first_name', 'name')

class DatasAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'asker_login', 'controler_login', 'controler_auth')

admin.site.register(Auth_users, UsersAdmin)
admin.site.register(Auth_datas, DatasAdmin)