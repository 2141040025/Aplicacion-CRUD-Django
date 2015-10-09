# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'profesores'},
        ),
        migrations.RemoveField(
            model_name='curso',
            name='profesor',
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ManyToManyField(to='new_app.Profesor'),
        ),
    ]
