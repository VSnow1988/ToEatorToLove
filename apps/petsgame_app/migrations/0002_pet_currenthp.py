# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsgame_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='currenthp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]