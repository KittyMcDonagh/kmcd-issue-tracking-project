# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-25 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2_user_home', '0011_auto_20191125_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='user_second_name',
            field=models.CharField(max_length=20),
        ),
    ]
