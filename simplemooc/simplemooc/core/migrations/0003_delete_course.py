# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171007_1605'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]
