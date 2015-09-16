# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('map_lng', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('map_lat', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('changed_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'map',
            },
        ),
    ]
