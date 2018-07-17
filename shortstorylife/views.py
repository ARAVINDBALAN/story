# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import story
# Create your views here.
def mainpage(request):
	return render(request,'shortstorylife/index.html')
def submit(request):
    story(title=request.GET.get("title"),content=request.GET.get("mine"),email=request.GET.get("email")).save()
    return render(request,'shortstorylife/index.html')	