# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160913_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories_descrption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='category_description2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Categories_descrption'),
        ),
    ]
