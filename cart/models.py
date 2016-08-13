from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ShoppingCart(models.Model):
    """
    Description:
        Class to store details of a ShoppingCart
    """
    user = models.ForeignKey(User, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
