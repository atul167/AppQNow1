
from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, default=None, unique=True, blank=True)
    otp = models.IntegerField(blank=True)
    otp_sent_time = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)
    otp_hashed = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True,db_index=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True,db_index=True)
