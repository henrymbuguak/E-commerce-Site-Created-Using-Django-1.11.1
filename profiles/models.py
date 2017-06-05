# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='Enter Description')
    '''
    location = models.CharField(max_length=120, default='Nairobi,Kenya',blank=True, null=True)
    job = models.CharField(max_length=120, null=True)
    '''
    def __unicode__(self):
        return self.name