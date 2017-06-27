# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-11 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sparql', models.TextField(verbose_name='SPARQL')),
                ('title', models.CharField(max_length=256, verbose_name='タイトル')),
                ('template', models.CharField(max_length=256, verbose_name='テンプレート')),
            ],
        ),
    ]
