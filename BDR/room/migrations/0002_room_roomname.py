# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomName',
            field=models.CharField(default='SALON_DEFAULT_NAME', max_length=16),
            preserve_default=False,
        ),
    ]
