# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0002_auto_20191015_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eContact',
            field=models.CharField(default=b'123', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eEmail',
            field=models.EmailField(default=b'123', max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eId',
            field=models.CharField(default=b'123', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eName',
            field=models.CharField(default=b'123', max_length=100),
        ),
    ]
