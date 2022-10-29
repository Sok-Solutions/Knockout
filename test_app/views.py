
from cgi import test
from multiprocessing import context
import random
from re import S
from turtle import right
from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import gamesss, questions
import random
import string
import json
# Create your views here.
def play(request):
    print("Started playing")
    quests = questions.objects.all()
    names = gamesss.objects.filter(gameid = request.session['gameid'])
    print(quests)
    print(names)
    questforweb = []
    i = 0
    while i < (len(quests)-1):
        if quests[i].withname == True:
            st = random.uniform(0, len(names))
            zwischen = quests[i].question.replace("#", names[int(st)].name)
            print(zwischen)
            questforweb.append([zwischen, i]) 
            print(questforweb[i])
        if quests[i].withname == False:
            questforweb.append([quests[i].question, i])
        i = i+1
    return render(request, 'play.html', {'quests' : questforweb})

def game(request):
    print("Game started!")
    if request.method == 'POST':
        print('Received data:', request.POST['Name'])
        gameidd = ''
        if request.session['gameid'] == 'a':
            gameidd = ''.join(random.choice(string.ascii_lowercase) for i in range(100))
        else:
            gameidd = request.session['gameid']
        gamesss.objects.create(gameid = gameidd, userid = request.user, name = request.POST['Name'])
        request.session['gameid'] = gameidd
    have_names = False

    all_names = gamesss.objects.filter(gameid = request.session['gameid'])
    if len(all_names) > 0:
        have_names = True
        print("Game REady")
    return render(request, 'game.html', {'all_names' : all_names, 'have_names' : json.dumps(have_names)})
def start(request):
    request.session['gameid']='a'
    numofq = 5
    print("hallo" + str(numofq))
    if request.method == 'POST':
        numofq = request.POST.get('numofq')
        request.session['numofquest'] = numofq
        print("hallo" + str(numofq))
    return render(request, 'index.html')

def loginpage(request):
    context = {
        'errmsg' : ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('succ')
            login(request, user) 
            return redirect('/start/')
        else:
            context = {
        'errmsg' : 'Password and/or Username wrong!'
    }
            print('notsucc')
    
            


    return render(request, 'login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('/login/')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/login/')

    context = {'form' :form}
    return render(request, 'register.html', context)
