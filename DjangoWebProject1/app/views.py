"""
Definition of views.
"""

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.template import RequestContext
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from email import (
    charset as Charset, encoders as Encoders, generator, message_from_string,
)
from app.models import *;

Charset.add_charset('utf-8',Charset.SHORTEST,None,'utf-8')

# method for representing existing Siths selection
def sithLog(request):
   
        siths = Sith.objects.all();

        cname = request.POST.get('dropdown1')
        if request.method == "GET": 
            form = SithForm()#placing the list of siths
            return render(request, 'app/sith.html', {'siths':siths})

        elif request.method == "POST":
            sithS = Sith.objects.get(nameSith=cname)  #save choosen siths as sithS
            id = sithS.id
            return HttpResponseRedirect(reverse( 'recruters', args=[id]))  #transfering sithS id to list recruits for this sith

# method for new recruit subscription
def recrutesubscribe(request):
    if request.method == "GET":
        form = RecrutesForm() #placing the form for recruit
        return render(request, 'app/subscribe.html', {'form':form})
    elif request.method == "POST":
        form = RecrutesForm(request.POST)
        data = form.save() #saving info in the form to recruit object
        id = data.id
        return HttpResponseRedirect(reverse( 'takeAquiz' , args=[id]))

# method for representing all quiz questions
def takeAquiz(request, id):
    quiz = Quiz.objects.all()
    recruter = Recrutes.objects.get(pk =id) #recruit who taking the quiz

    return render_to_response('app/quiz.html', {'quiz': quiz, 'recruter': recruter});

# method for answering specific questions of quiz
def vote(request, Pid,id):
     question = Quiz.objects.get(pk =id);        #specific questions of quiz
     recruter = Recrutes.objects.get(pk =Pid);    #for specific recruit who taking the quiz
     if request.method == "POST":
         selected_question = request.POST['question']
         if selected_question == question.optionTruequestion: #checking if the answer is right
                 question.answerTrue = True
                 question.resrutesWhoPass.add(recruter)    #add recruit to question parameter which store recruits who answered this question correctly
         elif selected_question != question.optionTruequestion:

                 question.answerTrue = False
         else:
              return HttpResponse(400, 'invalid form')
         question.save()
         return HttpResponseRedirect(reverse( 'takeAquiz' , args=[Pid]))
     


     return render(request,'app/vote.html', {'question': question, 'recruter': recruter});


# method for representing Recruits who took the test
def recruters(request, id):
    sithS = Sith.objects.get(pk=id) 
    count = sithS.resrutesShadowing.count()
    questions = Quiz.objects.all()
    recrList = []                  #list for recruit who took the test and not Shadowing
    allRecrutesWhoShadowing = [] #list for recruit who already ShadowHand
    sithAll = Sith.objects.all() 
    for s in sithAll:
        m = s.resrutesShadowing.all()
        for t in m:
            allRecrutesWhoShadowing.append(t)

    for rec in questions:
        Rlist = rec.resrutesWhoPass.all()
        for r in Rlist:
            if not(r in recrList) and not(r in allRecrutesWhoShadowing):
                recrList.append(r)       # Adding Recruits to list for recruit who took the test and not Shadowing

    return render_to_response('app/recruters.html', {'recrList': recrList, 'sithS': sithS, 'count':count});

# method for representing detail page of each Recruit who took the test
def recrutesdetails(request, id, Pid):
    recruter = Recrutes.objects.get(pk =id);
    sith = Sith.objects.get(pk =Pid);
   
    questions = Quiz.objects.all()
    TrueQuestionsList = []
    wrongList = []
    # look though each question to find right and wrong answered questions
    for question in questions:
        recruteList = question.resrutesWhoPass.all() # save Recruit who took the test in recruteList
        for r in recruteList:
            if r==recruter:
                TrueQuestionsList.append(question) # save in list right answered questions of this recruit

        if not(question in TrueQuestionsList):          
            wrongList.append(question) # save in list wrong answered questions of this recruit

  #  if "recruit" button was pressed we add this recruit to HandShadow of this Sith and send notification of acceptance to recruit
    if request.method == "POST":
         if sith.resrutesShadowing.count() < 3: #checking if this Sith have less than 3 recruits as Shadow Hand
             sith.resrutesShadowing.add(recruter) # add this recruit as Shadow Hand for this Sith
             sith.save()                          #save this Sith
             subject = 'Sith Order'
             message = "You've been accepted as a Shadow Hand. Once we were brothers in the Force. But from the Hundred-Year Darkness were born the Sith"
             recipientlist = recruter.planetRecruteEmail    # recruit email
             #send notification of acceptance to recruit through email
             send_mail( subject,message, settings.DEFAULT_FROM_EMAIL, [recipientlist,] , fail_silently=False)
             messages.success(request, 'Successfully Sent The Message!')

         else:
             messages.info(request, 'You already have 3 Shadow Hand, sorry, you can not recruit more', fail_silently=False)
    


    return render(request,'app/recrutdetail.html', {'recruter': recruter, 'recrList': TrueQuestionsList, 'wrongList': wrongList, 'sith': sith});


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Start',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact me',
            'message':'if you want to create an awesome Web, Desktop or Mobile application. I believe in power of programming to transform and improve our lives.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About me',
            'message':'Software Development Engineer',
            'year':datetime.now().year,
        }
    )
