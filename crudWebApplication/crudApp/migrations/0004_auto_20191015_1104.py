# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_auto_20191015_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eContact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eEmail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eId',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eName',
            field=models.CharField(max_length=100),
        ),
    ]
