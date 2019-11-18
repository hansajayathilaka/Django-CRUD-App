# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eId', models.CharField(max_length=20)),
                ('eName', models.CharField(max_length=100)),
                ('eEmail', models.EmailField(max_length=254)),
                ('eContact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
