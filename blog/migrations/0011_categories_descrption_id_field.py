# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160915_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories_descrption',
            name='id_field',
            field=models.IntegerField(default=0),
        ),
    ]
