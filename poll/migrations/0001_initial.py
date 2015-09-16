# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('pos', models.IntegerField()),
                ('content', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'option',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('select', models.IntegerField(null=True, blank=True)),
                ('type', models.IntegerField(null=True, blank=True)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('changed_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'poll',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('avatar', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('option', models.ForeignKey(to='poll.Option')),
                ('poll', models.ForeignKey(to='poll.Poll')),
            ],
            options={
                'db_table': 'vote',
            },
        ),
        migrations.AddField(
            model_name='option',
            name='poll',
            field=models.ForeignKey(to='poll.Poll'),
        ),
    ]
