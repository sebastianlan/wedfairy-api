# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20151013_1927'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='option',
            table=None,
        ),
        migrations.AlterModelTable(
            name='poll',
            table=None,
        ),
        migrations.AlterModelTable(
            name='vote',
            table=None,
        ),
    ]
