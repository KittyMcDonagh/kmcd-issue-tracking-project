# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-14 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_issue_logging', '0004_auto_20191112_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='software_component',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
