from django.db import models

from management.models import UserProfile

from product.models import Product

from oms.app_settings import (
    ORDER_STATUS, PAYMENT_MODE, CURRENCIES, DEFAULT_CURRENCY,
    DEFAULT_ORDER_STATUS, DEFAULT_PAYMENT_MODE)


class OrderMetaData(models.Model):
    """
    Common fields, all models in Order to extend this class
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
    	auto_now=True, editable=False, db_index=True)
    status = models.CharField(
        max_length=5, choices=ORDER_STATUS,
        default=DEFAULT_ORDER_STATUS, db_index=True)

    class Meta:
        abstract = True


class Order(OrderMetaData):
    """
    Class for order placed by the customer
    This class contains the details of an order placed by the customer
    from the website
    """
    order_id = models.CharField(max_length=255, db_index=True)

    # surrogate key - combination of client and order id to
    # uniquely identify the order in our database
    sk = models.CharField(
        max_length=255, unique=True, blank=True, null=True, editable=False)

    # billing details
    billing_user_details = models.ForeignKey(
        UserProfile, related_name='billing_user')

    # shipping details
    shipping_user_details = models.ForeignKey(UserProfile)

    # payment details
    payment_mode = models.CharField(
        max_length=1, choices=PAYMENT_MODE,
        default=DEFAULT_PAYMENT_MODE, db_index=True)

    # This is the net amount after all the taxes
    net_amount = models.DecimalField(
        max_digits=12, decimal_places=2,
        default=0.0)

    # This is the sum of mrp of all products in an order
    total_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)

    # This is the taxes involved
    total_taxes = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)

    shipping_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.0)

    currency = models.CharField(
        max_length=3, choices=CURRENCIES,
        default=DEFAULT_CURRENCY, null=True, blank=True)

    courier_name = models.CharField(
        max_length=255, blank=True, null=True)

    tracking_num = models.CharField(
        max_length=255, blank=True, null=True)

    total_qty = models.CharField(
        max_length=1024, blank=True, null=True)


class SubOrder(OrderMetaData):
    """
    Class to keep record of sub order of an order.
    Sub Order is basically an order containing same products of
    1 or more than 1 quantity
    """
    sub_order_id = models.CharField(max_length=255, db_index=True)

    order = models.ForeignKey(
    	Order, max_length=255, db_index=True, blank=True, null=True)

    prod_details = models.ForeignKey(Product)

    prod_qty = models.PositiveIntegerField(default=0)
