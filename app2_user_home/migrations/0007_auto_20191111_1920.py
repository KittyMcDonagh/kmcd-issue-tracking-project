# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-11 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2_user_home', '0006_filterforclientuser_filterforvenduser_statusfilter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FilterForClientUser',
        ),
        migrations.DeleteModel(
            name='FilterForVendUser',
        ),
        migrations.DeleteModel(
            name='StatusFilter',
        ),
    ]
