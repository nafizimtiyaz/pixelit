from App1.models import course,lecture
from django.db import models
from django.contrib.auth.models import User

class CART(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=1000)
    mycourse=models.TextField(max_length=1000)
    email=models.TextField(max_length=1000)
    TransectionID=models.CharField(max_length=100)
    Transection_Number=models.CharField(max_length=100)

    def __str__(self):
        return f'Name:{self.user} |  'f'Course: {self.mycourse}'