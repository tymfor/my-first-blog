# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-16 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160916_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='structuralmeasures',
            name='note_tech_11',
            field=models.TextField(default='will be updated', verbose_name='Note_applicability_Safety_during_construction'),
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='note_tech_12',
            field=models.TextField(default='will be updated', verbose_name='Note_applicability_Service life required'),
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='note_tech_13',
            field=models.TextField(default='will be updated', verbose_name='Note_applicability_Aesthetics'),
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='note_tech_14',
            field=models.TextField(default='will be updated', verbose_name='Note_applicability_TypicalCost'),
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='tech_11',
            field=models.IntegerField(default=0, verbose_name='Rate:11 Safety_during_construction'),
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='tech_12',
            field=models.IntegerField(default=0, verbose_name='Rate:12 Service life required'),
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='tech_13',
            field=models.IntegerField(default=0, verbose_name='Rate:13 Aesthetics'),
        ),
        migrations.AddField(
            model_name='structuralmeasures',
            name='tech_14',
            field=models.IntegerField(default=0, verbose_name='Rate:14 TypicalCost'),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='note_tech_10',
            field=models.TextField(default='will be updated', verbose_name='Note_applicability_Implementation'),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='note_tech_8',
            field=models.TextField(default='will be updated', verbose_name='Note_applicability_Reliability_peformance'),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='note_tech_9',
            field=models.TextField(default='will be updated', verbose_name='Note_applicability_Reliability_design'),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='tech_10',
            field=models.IntegerField(default=0, verbose_name='Rate:10 Implementation'),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='tech_8',
            field=models.IntegerField(default=0, verbose_name='Rate:8 Reliability_performance'),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='tech_9',
            field=models.IntegerField(default=0, verbose_name='Rate:9 Reliability_design'),
        ),
    ]
