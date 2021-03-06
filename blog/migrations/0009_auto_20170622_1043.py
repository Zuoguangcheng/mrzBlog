# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170616_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='更新时间'),
        ),
    ]
