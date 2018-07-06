from django.db import models

class Dog(models.Model):
    name=models.CharField(max_length=250)
    breed=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

