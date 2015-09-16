# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('avatar', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=50)),
                ('people', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'guest',
            },
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='rsvp',
        ),
        migrations.RemoveField(
            model_name='userrsvp',
            name='rsvp',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='changed_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 16, 17, 26, 39, 979395, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 16, 17, 26, 49, 528154, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='deadline',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='message',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='UserRsvp',
        ),
        migrations.AddField(
            model_name='guest',
            name='rsvp',
            field=models.ForeignKey(to='rsvp.Rsvp'),
        ),
    ]
