# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20150917_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='mobile',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
