from django.db import models

# Create your models here.
class mpcfragen(models.Model):
    text = models.CharField(max_length=255)
    c1 = models.CharField(max_length=255)
    c2 = models.CharField(max_length=255)
    c3 = models.CharField(max_length=255)
    c4 = models.CharField(max_length=255)
    right = models.IntegerField(default = 0)
class textfragen(models.Model):
    text = models.CharField(max_length=255)
    antwort = models.CharField(max_length=255)
class usertests(models.Model):
    user = models.CharField(max_length=255)
    anzahlfragen = models.IntegerField()
    richtig = models.IntegerField()
    falsch = models.IntegerField()