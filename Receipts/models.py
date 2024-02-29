from django.db import models

from Users.models import CustomUser

# Create your models here.

class Receipt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receipt_set')