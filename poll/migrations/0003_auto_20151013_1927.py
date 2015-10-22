# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_vote_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['pos']},
        ),
        migrations.AlterIndexTogether(
            name='option',
            index_together=set([('poll', 'pos')]),
        ),
    ]
