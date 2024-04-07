'''
   import HttpResponse from django.http to use it for returning response of any data.
   import BaseUserManager from django to create random tokens with length 32 char.
   import all tables ("Cla_User", "ClaTokens") from .models
   import requests to get some data 

'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.base_user import BaseUserManager
import requests
# Create your views here.
'''
   i use "@csrf_exempt" because when you make a request via a form you want 
   the form being submitted to your view to originate from your 
   website and not come from some other domain.(this is like security).
   the POST request method requests that a web server accepts the data enclosed
   in the body of the request message, most likely for storing it. It is often
   used when uploading a file or when submitting a completed web form
'''
CTF_ADDRESS = "http://127.0.0.1:7000"

# this function used to return random 32 chars of Tokens
@csrf_exempt
def get_token(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name', '')
        user_password = request.POST.get('user_password', '')
        # print(user_name, user_password)
        try:
            user = ClaUser.objects.get(user_name= user_name, user_password= user_password)
            # this checks if the user exist
            if user :
                old_tokens = ClaTokens.objects.filter(user=user)
                new_token = ClaTokens()
                new_token.user = user
                new_token.token = BaseUserManager().make_random_password(32) 
                # this checks if the user already have token 
                if len(old_tokens):
                    # make is_vaild = 0 
                    new_token.is_valid = False
                else:
                    # make is_vaild = 1
                    new_token.is_valid = True
                    data = {'token': new_token.token}
                    requests.post(f"{CTF_ADDRESS}/add_token/", data=data)
                # save tokens
                new_token.save()
                return HttpResponse(f"{new_token.token}")
            else:
                return HttpResponse("user not existed")
        except ClaUser.DoesNotExist:
            return HttpResponse("user not existed")
    return  HttpResponse("bad request")

