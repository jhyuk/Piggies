# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0037_auto_20170727_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='congressman',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='contents',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='pledge',
            name='tag',
        ),
        migrations.AlterField(
            model_name='comment',
            name='congressman',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
        migrations.AlterField(
            model_name='congressmanemotion',
            name='congressman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='congressman',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='congressman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
    ]
