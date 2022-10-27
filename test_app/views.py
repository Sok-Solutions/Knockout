from asyncio.windows_events import NULL
from multiprocessing import context
import random
from turtle import right
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import mpcfragen, textfragen, usertests
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.


def test(request):
    numofq = 5
    questions = mpcfragen.objects.all()
    quests = random.sample(range(1, 10), numofq)
    webquests = []
    answers = []
    i = 0
    for row in range(1):
        for col in range(5):
            i = i+1
            webquests.append([str(questions[quests[col]].text), str(questions[quests[col]].c1), str(questions[quests[col]].c2), str(questions[quests[col]].c3), str(questions[quests[col]].c4), str(questions[quests[col]].right), i])    
    if request.method == 'POST':
        answers.append(request.POST.get('answers'))
    print(answers)
    return render(request, 'test.html', {'webquests' : webquests})
def start(request):
    numofq = 5
    print("hallo" + str(numofq))
    if request.method == 'POST':
        numofq = request.POST.get('numofq')
        request.session['numofquest'] = numofq
        print("hallo" + str(numofq))
    else:
        if request.user.is_authenticated:
            request.session['loginf'] = 0
            print("test")
        else:
            request.session['loginf'] = 1
            return redirect('/login/')
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