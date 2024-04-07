
'''
   import HttpResponse from django.http to use it for returning response of any data.
   import all tables ("ValidTokens", "Vote") from .models
   import requests to get some data 
'''
from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.admin import ModelAdmin
from .models import *
from django.views.decorators.csrf import csrf_exempt

'''
   i use "@csrf_exempt" because when you make a request via a form you want 
   the form being submitted to your view to originate from your 
   website and not come from some other domain.(this is like security).
   the POST request method requests that a web server accepts the data enclosed
   in the body of the request message, most likely for storing it. It is often
   used when uploading a file or when submitting a completed web form
'''
# Create your views here.
# used to get tokens
@csrf_exempt
def add_token(request):
    if request.method == "POST":
        rec_token = request.POST.get('token', '')
        if len(rec_token) == 32:
            new_token = ValidTokens()
            new_token.token = rec_token
            new_token.save()
            return HttpResponse("added")

    return HttpResponse("error")
    
# this function is used to make real vote
@csrf_exempt
def vote_for(request):
    if request.method == "POST":
        choise = request.POST.get('vote_name', '')
        rec_token = request.POST.get('token', '')
        # check if token is exist:
        if ValidTokens.objects.filter(token=rec_token).exists():
            # check if the rec_token not in the vote table 
            if not Vote.objects.filter(token__token=rec_token).exists():
                # take object ftom table vote that will be used to inhert all thing in that table
                new_vote = Vote()
                new_vote.token = ValidTokens.objects.get(token=rec_token) #tag
                new_vote.for_whom = choise
                new_vote.save()
                return HttpResponse("valid")
            else:
                return HttpResponse("another vote")
        else:
            return HttpResponse("not valid token")
    return HttpResponse("")

# get numbers of votes for person1 and person2
@csrf_exempt   
def get_votes(request):
    # p1_votes = how many votes that person1 have
    p1_votes = len(Vote.objects.filter(for_whom="person1"))
    # p1_votes = how many votes that person1 have
    p2_votes = len(Vote.objects.filter(for_whom="person2"))
    # return response of html_page with number of votes of both persons
    return HttpResponse("""
    <html>
  <head>
    <title>Vote Election Booth</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js">
  </head>
  <body style="
  background: #9053c7;
  background: -webkit-linear-gradient(-135deg, #c850c0, #4158d0);
  background: -o-linear-gradient(-135deg, #c850c0, #4158d0);
  background: -moz-linear-gradient(-135deg, #c850c0, #4158d0);
  background: linear-gradient(-135deg, #c850c0, #4158d0);">
  <ul class="list-group" style="text-align: center;">
    <li class="list-group-item active ">Result </li>
    <li class="list-group-item list-group-item-danger ">Person1: {} Votes</li>
    <li class="list-group-item list-group-item-danger">Person2:  {} Votes</li>
  </ul>
    </body>
</html>""".format(p1_votes, p2_votes))
