from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django import forms
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Diet(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True)             
    calories_per_day = models.IntegerField()             
    is_vegetarian = models.BooleanField(default=False)    

