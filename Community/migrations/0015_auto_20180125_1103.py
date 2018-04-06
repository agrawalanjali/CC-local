# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0014_community_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='image',
        ),
        migrations.AddField(
            model_name='community',
            name='forum_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
