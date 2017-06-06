# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile, userStripe

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile

admin.site.register(Profile, profileAdmin)

class userStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = userStripe

admin.site.register(userStripe,  userStripeAdmin)

