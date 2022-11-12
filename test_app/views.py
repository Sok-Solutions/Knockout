
from cgi import test
from multiprocessing import context
import random
from re import S

from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import gamesss, questions, questionshot
import random
import string
import numpy as np
import json
import pyrebase



"""INITIALIZE FIREBASE"""
config={
    "apiKey": "AIzaSyDkTGod3Yh0fSlBPGPkdyLbxmYt0fZw9Rw",
    "authDomain": "knockout-2afbe.firebaseapp.com",
    "databaseURL": "https://knockout-2afbe-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "knockout-2afbe",
    "storageBucket": "knockout-2afbe.appspot.com",
    "messagingSenderId": "85603705850",
    "appId": "1:85603705850:web:88799d48ecc53bdb6b7a43",
    "measurementId": "G-VJDQDM84WW"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()



# Create your views here.

def firebase(request):
    channel_name = database.child('Data').child('Name').get().val()
    channel_city = database.child('Data').child('City').get().val()
    channel_age = database.child('Data').child('Age').get().val()
    return render(request, 'firebase.html', {
        "channel_name" : channel_name,
        "channel_age" : channel_age,
        "channel_city" : channel_city
    })

def postsignup(request):
    password2 = request.POST.get('password2')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if password == password2:
        if len(password) < 6:
                errormsg = "Das Passwort muss länger als 6 Zeichen sein!"
                return render(request, 'register.html', {'err' : errormsg})
        else:
            user = auth.create_user_with_email_and_password(email, password)
            return render(request, 'account/login.html')
    else:
        errormsg = "Die Passwörter stimmen nicht überein!"
        return render(request, 'register.html', {'err' : errormsg})

    
def startt(request):
    print("Logged in with google!")
    return redirect("/start/")

def postsigin(request):
    
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = auth.sign_in_with_email_and_password(email, password)
    request.session['idToken'] = user['idToken']
    return redirect("/start/")
def play(request):
    print(request.session['gamemode'])
    print("Started playing")
    quests = None
    if request.session['gamemode'] == "hot":
        quests = questionshot.objects.all()
        print("hot")
    if request.session['gamemode'] == "normal":
        print("normal")
        quests = questions.objects.all()  
    else:
        print("mode not defined")
        quests = questions.objects.all()  
    names = gamesss.objects.filter(gameid = request.session['gameid'])
    rand_questforweb = list(range(0, len(quests)))
    rand_questforweb = np.random.shuffle(rand_questforweb)
    questforweb = []
    print(rand_questforweb)
    print(len(quests))
    i = 0
    while i < (len(quests)):
        if quests[i].withname == True:
            st = random.randint(0, (len(names)-1))
            st2 = random.randint(0, (len(names)-1))
            while st2 == st:
                st2 = random.randint(0, (len(names)-1))
            print("st1:" + str(st) + " st2: " + str(st2))
            name1 = names[int(st)].name
            name2 = names[int(st2)].name
            if str(quests[i].question).count("#") == 1:
                if str(quests[i].question).count("§") == 1:
                    zwischen = quests[i].question.replace("#", name1)
                    print("ZWISCHEN1" + zwischen)
                    zwischen = zwischen.replace("§", name2)
                    print("ZWISCHEN1" + zwischen)
                    questforweb.append([zwischen, i]) 
                    print(questforweb[i])
                    print("Hallo")
                else:
                    zwischen = quests[i].question.replace("#", names[int(st)].name)
                    print(zwischen)
                    questforweb.append([zwischen, i]) 
                    print(questforweb[i])



        if quests[i].withname == False:
            questforweb.append([quests[i].question, i])
        i = i+1
    
    return render(request, 'play.html', {'quests' : questforweb})
def hot(request):
    request.session['gamemode'] = "hot"
    print("Game started!")
    if request.method == 'POST':
        print('Received data:', request.POST['Name'])
        gameidd = ''
        if request.session['gameid'] == 'a':
            gameidd = ''.join(random.choice(string.ascii_lowercase) for i in range(100))
        else:
            gameidd = request.session['gameid']
        gamesss.objects.create(gameid = gameidd, userid = request.user, name = request.POST['Name'])
        #database.child("Data").child("Games").push({"gameid" : gameidd})
        request.session['gameid'] = gameidd
    have_names = False

    all_names = gamesss.objects.filter(gameid = request.session['gameid'])
    if len(all_names) > 0:
        have_names = True
        print("Game REady")
    return render(request, 'hot.html', {'all_names' : all_names, 'have_names' : json.dumps(have_names)})
def game(request):
    request.session['gamemode'] = "normal"
    print("Game started!")
    if request.method == 'POST':
        print('Received data:', request.POST['Name'])
        gameidd = ''
        if request.session['gameid'] == 'a':
            gameidd = ''.join(random.choice(string.ascii_lowercase) for i in range(100))
        else:
            gameidd = request.session['gameid']
        gamesss.objects.create(gameid = gameidd, userid = request.user, name = request.POST['Name'])
        #database.child("Data").child("Games").push({"gameid" : gameidd})
        request.session['gameid'] = gameidd
    have_names = False

    all_names = gamesss.objects.filter(gameid = request.session['gameid'])
    if len(all_names) > 0:
        have_names = True
        print("Game REady")
    return render(request, 'game.html', {'all_names' : all_names, 'have_names' : json.dumps(have_names)})
def start(request):
    users = database.child("users").get()
    print(users.val())
    request.session['gameid']='a'

    if request.method == 'POST':
        numofq = request.POST.get('numofq')
        request.session['numofquest'] = numofq
        print("hallo" + str(numofq))
    user = request.session['idToken']
    print((auth.get_account_info(user)))
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
    return redirect('/accounts/login/')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/accounts//login/')

    context = {'form' :form}
    return render(request, 'register.html', context)

def gamechoice(request):
    return render(request, 'gamechoice.html')