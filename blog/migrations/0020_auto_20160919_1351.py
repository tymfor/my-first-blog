# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-19 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20160916_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Perform_weight_1',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='Perform_weight_2',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='Perform_weight_3',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='Perform_weight_4',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='Perform_weight_5',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='Perform_weight_6',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='Perform_weight_7',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='Perform_weight_8',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='available_measures_ahp_sume_peform_criteria',
            field=models.CommaSeparatedIntegerField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='figure_captions',
            field=models.CommaSeparatedIntegerField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='structuralmeasures',
            name='img_src',
            field=models.CommaSeparatedIntegerField(default=0, max_length=200),
        ),
    ]
