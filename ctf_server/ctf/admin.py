from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *
# Register your models here.
# admin.site.register(ValidTokens)
'''
   admin.site.register('Table_name or Class_name') is used to add tables in admin_Panel of django app
   admin.site.unregister('Table_name or Class_name') is used to remove tables in admin_Panel django app
   admin.site.site_header of 'any_thing' is used to change the default header dmin_Panel of django app
'''
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.disable_action('delete_selected')

'''
   @admin.register(table_name) is used to override the default permission of the admin_class.
   i have disabled the add, delete, change functionality as admin must not have any permission 
   to add, delete, change any tokens or any votes
'''
@admin.register(ValidTokens)
class AuthorAdmin(admin.ModelAdmin):
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False
    # This will help you to disbale delete functionality
    def has_delete_permission(self, request, obj = None):
        return False
    # This will help you to disbale change functionality
    def has_change_permission(self, request, obj = None):
        return False

@admin.register(Vote)
class AuthorAdmin(admin.ModelAdmin):
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj = None):
        return False
    def has_change_permission(self, request, obj = None):
        return False


