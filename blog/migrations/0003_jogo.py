# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-08 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_time_mascote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateTimeField()),
                ('Resultado', models.CharField(max_length=5)),
                ('Times', models.ManyToManyField(to='blog.Time')),
            ],
        ),
    ]
