# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-20 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20160924_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        # migrations.AlterField(
        #     model_name='answer',
        #     name='question',
        #     field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='database.Question'),
        # ),
    ]
