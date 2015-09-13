# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'id', primary_key=True)),
                ('user_pic_url', models.TextField()),
                ('name', models.TextField()),
                ('people', models.IntegerField()),
                ('create_date', models.DateField()),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'id', primary_key=True)),
                ('message', models.TextField()),
                ('deadline', models.DateField()),
            ],
            options={
                'db_table': 'rsvp',
            },
        ),
        migrations.CreateModel(
            name='UserRsvp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'id', primary_key=True)),
                ('user', models.IntegerField()),
                ('rsvp', models.ForeignKey(to='rsvp.Rsvp')),
            ],
            options={
                'db_table': 'user_rsvp',
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='rsvp',
            field=models.ForeignKey(to='rsvp.Rsvp'),
        ),
    ]
