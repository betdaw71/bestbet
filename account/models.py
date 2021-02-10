from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#
# def pkgen():
#     from base64 import b32encode
#     from hashlib import sha1
#     from random import random
#     rude = ('lol',)
#     bad_pk = True
#     while bad_pk:
#         pk = b32encode(sha1(str(random()).encode('utf-8')).digest()).lower()[:6]
#         bad_pk = False
#         for rw in rude:
#             if pk.find(rw) >= 0: bad_pk = True
#     return pk
import uuid
from time import timezone
class User(AbstractUser):
    username = models.CharField(blank=True,max_length=150,unique=True)
    email = models.EmailField('Email', unique=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(auto_now=True,null=True, blank=True)
    CURRENCY_CHOICES = [
        ('EUR', 'Euro'),
        ('USD', 'Dollar'),
        ('RUB', 'Ruble'),
    ]
    currency = models.CharField('Валюта',
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='RUB',
    )
    number = models.IntegerField(default=7)
    # bill_id = models.CharField(max_length=6, primary_key=True, default=pkgen)
    email_confirm = models.BooleanField(default=False)
    identification = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='account',default='default-user.jpeg')
    bill_id=models.CharField(max_length=100, null=True, blank=True, unique=True)
    balance = models.IntegerField(default=0)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    # def __init__(self):
    #      AbstractUser.__init__(self)
    #      self.bill_id = str(uuid.uuid4())

    # class Meta:
    #     app_label = 'auth'
