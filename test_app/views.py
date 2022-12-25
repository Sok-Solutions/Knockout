

import random
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import questions, koo, questionshot, gamesss, casuall, duelll
import random as rd
import string
import json

import random
from django.http import HttpResponseRedirect







# Create your views here.
def getcommand(request):
    normal_data = list(questions.objects.all())
    causal_data = list(casuall.objects.all())
    hot_data = list(questionshot.objects.all())
    ko_data = list(koo.objects.all())
    duell_data = list(duelll.objects.all())
    return render(request, 'getcommand.html', {'data_0815' : normal_data, 'data_casual' : causal_data, 'data_hot' : hot_data, 'data_ko' : ko_data, 'data_duell' : duell_data})

def questiondb1(request):
    modus = "0815"
    all_items = questions.objects.all()
    return render(request ,'questiondb.html', {'all_items' : all_items, 'modus' : modus})
def questiondb2(request):
    modus = "Duell"
    all_items = duelll.objects.all()
    return render(request ,'questiondb.html', {'all_items' : all_items, 'modus' : modus})
def questiondb3(request):
    modus = "K.O."
    all_items = koo.objects.all()
    return render(request ,'questiondb.html', {'all_items' : all_items, 'modus' : modus})
def questiondb4(request):
    modus = "Casual"
    all_items = casuall.objects.all()
    return render(request ,'questiondb.html', {'all_items' : all_items, 'modus' : modus})
def questiondb5(request):
    modus = "Hot"
    all_items = questionshot.objects.all()
    return render(request ,'questiondb.html', {'all_items' : all_items, 'modus' : modus})
def warn(request):
    request.session['warning'] = 1
    print('warning was accepted!')
    return render(request, 'warn.html')

def admind(request):
    games = gamesss.objects.all()
    User = get_user_model()
    users = len(User.objects.all())
    Normal = len(questions.objects.all())
    print(Normal)
    Duell = len(duelll.objects.all()) 
    ko = len(koo.objects.all())
    Casual = len(casuall.objects.all())
    Hot = len(questionshot.objects.all())
    i = 0
    gamesequal = []
    gamenum = 0
    
    while i < len(games):
        
        if games[i].gameid in gamesequal:
            print("Already")
        else:
            gamesequal.append(games[i].gameid)
            gamenum = gamenum + 1
       
        
        i = i + 1
    
    return render(request, 'admind.html', {'Normal' : Normal, 'duell' : Duell, 'KO' : ko, 'Casual' : Casual, 'Hot' : Hot, 'users' : users, 'games' : gamenum})
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
    print("Started playing")
    quests = None
    if request.session['gamemode'] == "hot":
        quests = questionshot.objects.all()
        print("hot")
    if request.session['gamemode'] == "normal":
        print("normal")
        quests = questions.objects.all()
    if request.session['gamemode'] == "duell":
        print("normal")
        quests = duelll.objects.all()  
    if request.session['gamemode'] == "ko":
        print("normal")
        quests = koo.objects.all()
    if request.session['gamemode'] == "casual":
        print("normal")
        quests = casuall.objects.all()
    names = gamesss.objects.filter(gameid = request.session['gameid'])
    rand_questforweb = []
    i = 0
    while i < len(quests):
        rand_questforweb.append(i)
        i = i+1
    print("RANDOMQUESTS:")
    print(rand_questforweb)
    rand_questforweb = random.sample(list(rand_questforweb), len(rand_questforweb))
    
    print("RANDOMQUESTS:")
    print(rand_questforweb)
    print("LAENGE" + str(len(quests)))
    questforweb = []
    rq = rand_questforweb
    i = 0
    while i < (len(quests)):
        print("ASJDHLKAJSDHAKLSHD" + str(i))
        print("Withname: " + str(quests[rq[i]].withname))
        if quests[rq[i]].withname == True:
            st = random.randint(0, (len(names)-1))
            st2 = random.randint(0, (len(names)-1))
            while st2 == st:
                st2 = random.randint(0, (len(names)-1))
            print("st1:" + str(st) + " st2: " + str(st2))
            name1 = names[int(st)].name
            name2 = names[int(st2)].name
            if str(quests[rq[i]].question).count("#") == 1:
                if str(quests[rq[i]].question).count("§") == 1:
                    zwischen = quests[rq[i]].question.replace("#", name1)
                    print("ZWISCHEN1" + zwischen)
                    zwischen = zwischen.replace("§", name2)
                    print("ZWISCHEN1" + zwischen)
                    questforweb.append([zwischen, i]) 
                    print("Hallo")
                else:
                    zwischen = quests[rq[i]].question.replace("#", names[int(st)].name)
                    print(zwischen)
                    questforweb.append([zwischen, i]) 
        if quests[rq[i]].withname == False:
            print(quests[rq[i]].question)
            questforweb.append([quests[rq[i]].question, i])
        i = i+1
    print("QUESTSFORWEB:")
    print(questforweb)
    last = len(questforweb)
    print(last)
    return render(request, 'play.html', {'quests' : questforweb, 'last' : last})
def hot(request):
    request.session['gamemode'] = "hot"
    request.session.modified = True
    print("1" + request.session['gamemode'])
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
def ko(request):
    request.session['gamemode'] = "ko"
    request.session.modified = True
    print("1" + request.session['gamemode'])
    print("Game started!")
    
    if request.method == 'POST':
        print('Received data:', request.POST['Name'])
        gameidd = request.session['gameid']
        gamesss.objects.create(gameid = gameidd, userid = request.user, name = request.POST['Name'])
        #database.child("Data").child("Games").push({"gameid" : gameidd})
        request.session['gameid'] = gameidd
    have_names = False

    all_names = gamesss.objects.filter(gameid = request.session['gameid'])
    if len(all_names) > 0:
        have_names = True
        print("Game REady")
    return render(request, 'ko.html', {'all_names' : all_names, 'have_names' : json.dumps(have_names)})
def duell(request):
    request.session['gamemode'] = "duell"
    request.session.modified = True
    print("1" + request.session['gamemode'])
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
    return render(request, 'duell.html', {'all_names' : all_names, 'have_names' : json.dumps(have_names)})
def casual(request):
    request.session['gamemode'] = "casual"
    request.session.modified = True
    print("1" + request.session['gamemode'])
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
    return render(request, 'casual.html', {'all_names' : all_names, 'have_names' : json.dumps(have_names)})
def game(request):
    request.session['gamemode'] = "normal"
    request.session.modified = True
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
    request.session['gameid']='a'

    if request.method == 'POST':

        numofq = request.POST.get('numofq')
        request.session['numofquest'] = numofq
        request.session['gameid'] = ''.join(random.choice(string.ascii_lowercase) for i in range(100))
        print("hallo" + str(numofq))
    #user = request.session['idToken']
    #print((auth.get_account_info(user)))
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
def addName(request):
    if request.POST['contentko'] != "":
        name = request.POST['contentko']
        gameidd = request.session['gameid']
        if name == "":
            print("NAME IS EMPTY")
        else:
            gamesss.objects.create(gameid = gameidd, userid = request.user, name = name)
        return HttpResponseRedirect('/ko/')
def addNameCasual(request):
    if request.POST['contentko'] != "":
        name = request.POST['contentko']
        gameidd = request.session['gameid']
        if name == "":
            print("NAME IS EMPTY")
        else:
            gamesss.objects.create(gameid = gameidd, userid = request.user, name = name)
        return HttpResponseRedirect('/casual/')   
def addNameDuell(request):
    if request.POST['contentko'] != "":
        name = request.POST['contentko']
        gameidd = request.session['gameid']
        if name == "":
            print("NAME IS EMPTY")
        else:
            gamesss.objects.create(gameid = gameidd, userid = request.user, name = name)
        return HttpResponseRedirect('/duell/')   
def addNameNormal(request):
    if request.POST['contentko'] != "":
        name = request.POST['contentko']
        gameidd = request.session['gameid']
        if name == "":
            print("NAME IS EMPTY")
        else:
            gamesss.objects.create(gameid = gameidd, userid = request.user, name = name)
        return HttpResponseRedirect('/game/')   
def addNameHot(request):
    if request.POST['contentko'] != "":
        name = request.POST['contentko']
        gameidd = request.session['gameid']
        if name == "":
            print("NAME IS EMPTY")
        else:
            gamesss.objects.create(gameid = gameidd, userid = request.user, name = name)
        return HttpResponseRedirect('/hot/')   

def deleteTodoView(request, i):
    y = gamesss.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/game/') 
def deleteTodoViewCasual(request, i):
    y = gamesss.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/casual/')
def deleteTodoViewDuell(request, i):
    y = gamesss.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/duell/')
def deleteTodoViewHot(request, i):
    y = gamesss.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/hot/')   
def deleteTodoViewKo(request, i):
    y = gamesss.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/ko/') 
def inserttabels(request):
    user = str(request.user)
    if request.user.is_authenticated:
        if request.method == "POST":
            file2 = request.POST.get('file')
            print(file2)
            readstring = file2
            readstring = readstring.split("@")
            teststring = []
            i = 0
            while i < len(readstring):
                if "#" in str(readstring[i]):
                    teststring.append([readstring[i], True])
                else:
                    if "§" in str(readstring[i]):
                        teststring.append([readstring[i], True])
                    else:
                        teststring.append([readstring[i], False])
                i = i + 1
            print(teststring)

            i = 0
            while len(teststring) > i:
                print(questions.objects.create(question = teststring[i][0], withname = teststring[i][1]))
                i = i+1
    else:
        return redirect('/admin/')

    return render(request, 'inserttabels.html')

