# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 07:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cast', '0006_auto_20170621_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='congressman',
            name='emotion',
            field=models.ManyToManyField(through='cast.CongressmanEmotion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pledge',
            name='emotion',
            field=models.ManyToManyField(through='cast.PledgeEmotion', to=settings.AUTH_USER_MODEL),
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