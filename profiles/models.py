# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class Profile(models.Model):
    name = models.CharField(max_length=120)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    description = models.TextField(default='Enter Description')
    '''
    location = models.CharField(max_length=120, default='Nairobi,Kenya',blank=True, null=True)
    job = models.CharField(max_length=120, null=True)
    '''
    def __unicode__(self):
        return self.name

class userStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null= True, blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username

"""
def my_callback(sender,request,user, **kwargs):
    idStripe, created = userStripe.objects.get_or_create(user=user)
    if created:
        print 'created for %s'%(user.username)

    userProfile, is_created = Profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()
"""


def stripeCallback(sender, request, user, **kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user=user)
    if created:
        print 'created for %s' % (user.username)
    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=user.email)
        user_stripe_account.stripe_id = new_stripe_id['id']
        user_stripe_account.save()

def profileCallback(sender, request, user, **kwargs):
    userProfile, is_created = Profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()


user_logged_in.connect(stripeCallback)
user_signed_up.connect(profileCallback)
