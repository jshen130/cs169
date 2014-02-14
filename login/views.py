from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from login.models import User
import mvc
import json

def index(request):
    return render_to_response('login/index.html', {'users' : User}, RequestContext(request))

def add(request):
    if request.method == 'POST':
        user_field = request.POST.get('username')
        pass_field = request.POST.get('password')
        existing_user = User.objects.filter(username=user_field)
        existing_user = existing_user[0] if existing_user else None
        error = mvc.SUCCESS
        if user_field and len(user_field) < mvc.MAX_USERNAME_LENGTH:
            # username field non empty -> existing user or new user
            if request.POST.get('login') is not None: # user clicked login
                print "login"
                if existing_user and existing_user.password == pass_field: # correct user/pass pair
                    existing_user.counter += 1
                    existing_user.save()
                    print "update"
                else:
                    error = mvc.ERR_BAD_CREDENTIALS
                    print "wrong pass"
            elif request.POST.get('add') is not None: # user clicked add
                print "add"
                if existing_user:
                    error = mvc.ERR_USER_EXISTS
                    print "exists"
                elif len(pass_field) > mvc.MAX_PASSWORD_LENGTH:
                    error = mvc.ERR_BAD_PASSWORD
                    print "badpass"
                else:
                    existing_user = User(username=user_field, password=pass_field, counter=1)
                    print "new user!"
                    existing_user.save()
            else:
                print "huh"
        else:
            error = mvc.ERR_BAD_USERNAME
        print existing_user
        return render_to_response('login/add.html',
                                  {'user' : existing_user,
                                   'error': error,}, RequestContext(request))
    else:
        return HttpResponse("Not a POST response")
