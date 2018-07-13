# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
# Create your models here.
class story(models.Model):
    email = models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100,null=True)
    content=models.CharField(max_length=400,null=True)
   	
    def __str__(self):
        return self.user


