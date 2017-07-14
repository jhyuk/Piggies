# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-05 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0013_auto_20170626_1750'),
    ]

    operations = [
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
            model_name='pledge',
            name='congressman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.Congressman'),
        ),
    ]
