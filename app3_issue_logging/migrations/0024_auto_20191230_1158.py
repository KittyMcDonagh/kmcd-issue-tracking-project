# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-30 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_issue_logging', '0023_issuethumbsup_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuecomment',
            name='comments',
            field=models.CharField(max_length=200),
        ),
    ]
