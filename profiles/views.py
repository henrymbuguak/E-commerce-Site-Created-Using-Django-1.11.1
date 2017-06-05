# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    context = {}
    templates = 'home.html'
    return render(request,templates,context)

def about(request):
    context = {}
    templates = 'about.html'
    return render(request,templates,context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    templates = 'profile.html'
    return render(request,templates,context)
