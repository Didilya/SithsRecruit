"""
Definition of models.
"""

from django.db import models
from django import forms
from django.forms import ModelForm
from django.views.generic import CreateView

class Planet(models.Model):
    planetName = models.CharField("Planet",max_length=64)


class Recrutes(models.Model):
    nameRecrut = models.CharField("Recrut",max_length=64)
    planetRecrute = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name = "localRecrutes")
    recruteAge = models.PositiveIntegerField(default=0)
    planetRecruteEmail = models.CharField("Email",max_length=64)



class Sith(models.Model):
    nameSith = models.CharField("Sith",max_length=64)
    planetSithTeaching = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name = "localSiths")
    resrutesShadowing = models.ManyToManyField(Recrutes, blank=True)

class RecrutesForm(forms.ModelForm):
    class Meta:
        model = Recrutes
        
        fields = ['nameRecrut','planetRecrute','recruteAge','planetRecruteEmail']
        widgets = {
          
           'planetRecruteEmail': forms.EmailInput(attrs = { 
               'class': 'form-control', 'placeholder': 'your@email.ru', 
           }),
       }

class SithForm(forms.ModelForm):
   class Meta:
       model = Sith
       fields = ['nameSith']
      
      

class Quiz(models.Model):
    question = models.TextField()
    optionYes = models.CharField(default="Yes",max_length = 30)
    optionNo = models.CharField(default="No",max_length = 30)
    optionTruequestion = models.CharField(default="Yes",max_length = 30)
    resrutesWhoPass = models.ManyToManyField(Recrutes, blank=True)
    answerTrue = models.BooleanField(blank=True, default= False)
    answerWrong = models.BooleanField(blank=True, default= False)
