# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 16:39
from __future__ import unicode_literals

from django.db import migrations,models
import datetime

def change_data(apps, schema_editor):
    Elly = apps.get_model("elly", "Elly")    
    print "nada"

class Migration(migrations.Migration):

    dependencies = [
        ('elly', '0004_elly_socialhed'),
    ]

    operations = [
        migrations.RunPython(change_data),
    ]
