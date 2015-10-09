# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_auto_20150930_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='imagen',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=b'profesores/img'),
            preserve_default=False,
        ),
    ]
