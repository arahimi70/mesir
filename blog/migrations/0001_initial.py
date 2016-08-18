# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField()),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('meta_description', models.CharField(max_length=155, verbose_name='Meta description for SEO')),
                ('keywords', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'verbose_name': 'Blog',
                'ordering': ['created'],
            },
        ),
    ]
