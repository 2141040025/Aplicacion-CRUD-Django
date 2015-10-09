# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_auto_20150930_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
