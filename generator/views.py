from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):

    thepassword1=''


    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=-'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
        



    theLength=int(request.GET.get('lengthOfPassword'))



    for x in range(theLength):
        thepassword1 +=random.choice(characters)

    return render(request,'generator/password.html', {'pass':thepassword1})

def about(request):
    return render(request,'generator/about.html')