# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'aidaijia_coupon',
            },
        ),
        migrations.CreateModel(
            name='CouponCandidate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('used', models.IntegerField()),
            ],
            options={
                'db_table': 'aidaijia_coupon_candidate',
            },
        ),
    ]
