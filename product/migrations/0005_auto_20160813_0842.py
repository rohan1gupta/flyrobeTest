# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[(b'ALL', b'ALL'), (b'XXS', b'XXS'), (b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'FS', b'FREESIZE')], default=b'XL', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='product.ProductColor'),
        ),
    ]
