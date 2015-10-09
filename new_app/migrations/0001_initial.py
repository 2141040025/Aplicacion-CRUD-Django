# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=30)),
                ('departamento', models.ForeignKey(to='new_app.Departamento')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(to='new_app.Profesor'),
        ),
    ]
