# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-11 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3_issue_logging', '0002_auto_20191111_1552'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FilterForVendUser',
            new_name='FilterForClient',
        ),
        migrations.RenameModel(
            old_name='FilterForClientUser',
            new_name='FilterForVendor',
        ),
        migrations.RenameField(
            model_name='filterforclient',
            old_name='filter_vend_desc',
            new_name='filter_value',
        ),
        migrations.RenameField(
            model_name='filterforvendor',
            old_name='filter_client_desc',
            new_name='filter_value',
        ),
    ]
