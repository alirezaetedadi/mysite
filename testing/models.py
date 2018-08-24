from django.db import models

class views(models.Model):
    user_ip = models.CharField(max_length=20)
    count = models.IntegerField(default=0)\

