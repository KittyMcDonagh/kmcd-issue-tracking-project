# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-25 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2_user_home', '0007_auto_20191111_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_name',
            field=models.CharField(max_length=6),
        ),
    ]
