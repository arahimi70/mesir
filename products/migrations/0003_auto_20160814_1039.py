# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
