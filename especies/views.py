# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Especie

def index(request):
    especies = Especie.objects.all()
    context = {'especies': especies}
    return render(request, 'especies/index.html', context)
