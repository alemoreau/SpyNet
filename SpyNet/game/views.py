#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.


def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = u"""<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


def date_actuelle(request):
    return render(request, 'game/date.html', {'date': datetime.now()})
