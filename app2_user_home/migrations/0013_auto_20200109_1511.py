# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-09 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2_user_home', '0012_auto_20191125_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='user_contact_nr',
            new_name='client_contact_nr',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='user_email_addr',
            new_name='client_email_addr',
        ),
    ]