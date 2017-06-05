# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile

admin.site.register(Profile, profileAdmin)