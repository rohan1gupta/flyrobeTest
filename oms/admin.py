from django.contrib import admin

from models import Order


class OrderAdmin(admin.ModelAdmin):
    """
    Description:
        admin for Users
    """
    search_fields = ['name']
    model = Order

admin.site.register(Order, OrderAdmin)
