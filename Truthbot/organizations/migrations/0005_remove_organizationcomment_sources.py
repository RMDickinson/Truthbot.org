# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-20 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20160617_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationcomment',
            name='sources',
        ),
    ]