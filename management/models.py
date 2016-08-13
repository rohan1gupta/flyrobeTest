from django.db import models
from django.contrib.auth.models import User

from management.app_settings import USER_TYPES, DEFAULT_USER_TYPE


class UserProfile(models.Model):
    """
    """
    # This field stores the user details like username, password,
    # firstname, lastname, email, date_joined
    user = models.OneToOneField(User)
    user_type = models.CharField(
        choices=USER_TYPES, default=DEFAULT_USER_TYPE, max_length=255)
    add1 = models.CharField(max_length=500, null=True, blank=True)
    add2 = models.CharField(max_length=500, null=True, blank=True)
    pin = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    phone1 = models.CharField(max_length=20, blank=True, null=True)
    phone2 = models.CharField(max_length=20, blank=True, null=True)


class Client(models.Model):
    """
    Abstract class to capture some common fields
    """
    name = models.CharField(
        max_length=255, blank=True, null=True)
    address1 = models.CharField(
        "Address line 1", max_length=500,
        null=True, blank=True)
    address2 = models.CharField(
        "Address line 2", max_length=500,
        null=True, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    phone1 = models.CharField(
        blank=True, max_length=14, null=True)
    phone2 = models.CharField(
        blank=True, max_length=14, null=True)
    email = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(
    	auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(
    	auto_now=True, editable=False, db_index=True)
    user_profile = models.ForeignKey(
        UserProfile, limit_choices_to={'user_type': 'SUP'})


    def __unicode__(self):
        return self.name
