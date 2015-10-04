from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.
def register_view(request):
    username = request.POST['username']
    ps1 = request.POST['password1']
    ps2 = request.POST['password2']

    if User.objects.filter(username=username).count() > 0:
        return HttpResponseRedirect('/?msg=err_already')
    elif ps1 != ps2:
        return HttpResponseRedirect('/?msg=err_checkps')
    else:
        User.objects.create_user(username, 'email', ps1)
        user = authenticate(username=username, password=ps1)
        login(request, user)
        return HttpResponseRedirect('/')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/?msg=err_login')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def submit_view(request):
    flag = request.POST['flag']
    stage = Stage.objects.filter(flag=flag)
    if stage.count() > 0:
        stage = stage[0]
        request.user.participant.cleared_stages.add(stage)
    
    return HttpResponseRedirect('/')

def main_page(request):
    stages = Stage.objects.all()
    players = Participant.objects.all().annotate(score=Count('cleared_stages')).order_by('-score', 'submit_time')
    msg = request.GET.get('msg', '');
    return render(request, 'main.html', {'msg': msg, 'stages': stages, 'players': players})
