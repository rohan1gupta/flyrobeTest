from django.db import models

from product.app_settings import *

from management.models import Client

from cart.models import ShoppingCart


# from django_autoslug.fields import AutoSlugField


class ProductCategory(models.Model):
    """
    """
    category_name = models.CharField(max_length=255)


class ProductOccasion(models.Model):
    """
    """
    occasion = models.CharField(max_length=255)


class ProductColor(models.Model):
    """
    """
    color = models.CharField(max_length=255)


class Product(models.Model):
    """
    """
    name = models.CharField(
        max_length=255, blank=True, null=True, db_index=True)
    number = models.CharField(
        max_length=255, blank=True, null=True,
        db_index=True)
    size = models.CharField(
        choices=SIZES, default=DEFAULT_SIZE,
        max_length=5, blank=True, null=True)
    brand = models.CharField(max_length=255, db_index=True)
    sku = models.CharField(max_length=255, db_index=True)

    rent_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    value_price = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)

    url = models.URLField(null=True, blank=True)

    description = models.TextField(blank=True, null=True)

    quantity = models.PositiveIntegerField(default=0)

    client = models.ForeignKey(
        Client, limit_choices_to={'active': True},
        on_delete=models.PROTECT, null=True, blank=True)
    shop_cart = models.ForeignKey(ShoppingCart, null=True, blank=True)

    category = models.ManyToManyField(ProductCategory, blank=True)
    occasion = models.ManyToManyField(ProductOccasion, blank=True)
    color = models.ManyToManyField(ProductColor, blank=True)
