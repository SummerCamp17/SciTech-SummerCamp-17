# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170507_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.IntegerField(choices=[(1, 'Available'), (0, 'Issued')]),
        ),
    ]
