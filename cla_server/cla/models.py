'''
   import database from django to create tables 
   import BaseUserManager from django to create random tokens with length 32 char

'''
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
'''
   create "ClaUser" table (data base for user)
   create "ClaTokens" table (data base for Api_Tokens)
   
'''


# Create your models here.
class ClaUser(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    user_password = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.user_name


class ClaTokens(models.Model):
    token = models.CharField(max_length=32, default=BaseUserManager().make_random_password(32), blank=True, unique_for_date="pub_date")
    is_valid = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(ClaUser,on_delete=models.CASCADE)
    def __str__(self):
        return self.token

