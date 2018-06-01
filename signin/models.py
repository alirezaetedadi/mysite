from django.db import models

class sign_in(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField()
    email = models.EmailField(blank=True)
    number = models.IntegerField(blank=True, null=True)