# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-13 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_map_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='map',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
