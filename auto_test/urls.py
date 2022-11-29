"""auto_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from test_app.views import start, loginpage, logoutuser, register, startt, game, play, firebase, postsigin, postsignup, gamechoice, hot, ko, duell, casual, warn, addName, addNameCasual, addNameDuell, addNameNormal, addNameHot, deleteTodoView, deleteTodoViewCasual, deleteTodoViewDuell, deleteTodoViewHot, deleteTodoViewKo
from django.views.generic.base import TemplateView



urlpatterns = [
    path('deleteTodoItemCasual/<int:i>/', deleteTodoViewCasual),
    path('deleteTodoItemDuell/<int:i>/', deleteTodoViewDuell),
    path('deleteTodoItemHot/<int:i>/', deleteTodoViewHot),
    path('deleteTodoItemKo/<int:i>/', deleteTodoViewKo),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('addNameHot/', addNameHot),
    path('addNameNormal/', addNameNormal),
    path('addNameDuell/', addNameDuell),
    path('addName/', addName),
    path('addNameCasual/', addNameCasual),
    path('warn/', warn, name='warn'),
    path('hot/', hot, name='hot'),
    path('ko/', ko , name='ko'),
    path('duell/', duell, name='duell'),
    path('casual/', casual, name='casual'),
    path('choice/', gamechoice, name='choice'),
    path('admin/', admin.site.urls),
    path('play/', play, name='play'),
    path('fire/', firebase, name='fire'),
    path('login/', loginpage, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('game/', game, name = 'game'),
    path('register/', register, name = 'register'),
    path('start/', start, name='start'),
    re_path(r'^$', start, name='index'),
    re_path('accounts/profile/', startt),
    path('postsignin/', postsigin, name='postsignin'),
    path('postsignup/', postsignup, name="postsignup")
]
