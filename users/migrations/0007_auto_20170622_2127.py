# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-22 21:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170620_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 22, 21, 27, 40, 18258, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 22, 21, 27, 40, 18602, tzinfo=utc)),
        ),
    ]