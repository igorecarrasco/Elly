# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elly', '0003_remove_elly_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='elly',
            name='socialhed',
            field=models.TextField(default=''),
        ),
    ]
