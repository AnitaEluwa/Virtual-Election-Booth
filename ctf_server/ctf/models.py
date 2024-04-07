'import database from django to create tables'

from django.db import models

# Create your models here.
'''
   create "ValidTokens" table (data base for Vaild_Tokens that have permission for voting)
   create "Vote" table (data base for Voting)
'''
class ValidTokens(models.Model):
    token = models.CharField(max_length=100, null= False, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.token


class Vote(models.Model):
    for_whom = models.CharField(max_length=100, null= False)
    added_at = models.DateTimeField(auto_now_add=True)
    token = models.ForeignKey(ValidTokens,on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.for_whom}')
