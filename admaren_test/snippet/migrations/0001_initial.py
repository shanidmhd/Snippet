# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-09-24 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_content', models.TextField(blank=True, null=True)),
                ('dat_created', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('pk_bint_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vchr_title', models.CharField(blank=True, max_length=100, unique=True)),
            ],
        ),
    ]
