# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='client',
        ),
    ]
