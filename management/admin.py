from django.contrib import admin

from models import Client, UserProfile


class ClientAdmin(admin.ModelAdmin):
    """
    Description:
        admin for Clients
    """
    list_filter = ['name']
    list_display = ["name"]
    search_fields = ["name"]
    model = Client


class UserProfileAdmin(admin.ModelAdmin):
    """
    Description:
        admin for Users
    """
    search_fields = ['name']
    model = UserProfile

admin.site.register(Client, ClientAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
