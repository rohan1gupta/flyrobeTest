# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='sk',
        ),
    ]
