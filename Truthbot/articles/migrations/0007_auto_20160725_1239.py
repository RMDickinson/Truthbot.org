# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_loggedarticlereviewedit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggedarticlereviewedit',
            name='review',
        ),
        migrations.RemoveField(
            model_name='loggedarticlereviewedit',
            name='user',
        ),
        migrations.DeleteModel(
            name='LoggedArticleReviewEdit',
        ),
    ]