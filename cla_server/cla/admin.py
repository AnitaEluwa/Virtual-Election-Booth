'''
   import admin_class from django.contrib
   import Group, User from django.contrib.auth.models
   import Cla_User from .Models 
'''
from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *
# Register your models here.
'''
   admin.site.register('Table_name or Class_name') is used to add tables in admin_Panel of django app
   admin.site.unregister('Table_name or Class_name') is used to remove tables in admin_Panel django app
   admin.site.site_header of 'any_thing' is used to change the default header dmin_Panel of django app
'''
admin.site.register(ClaUser)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = 'Add Cla_User'

