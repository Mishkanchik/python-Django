from django.db import models

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
