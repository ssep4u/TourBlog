# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-04 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180804_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
