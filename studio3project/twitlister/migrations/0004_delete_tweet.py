# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitlister', '0003_auto_20161013_1107'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tweet',
        ),
    ]
