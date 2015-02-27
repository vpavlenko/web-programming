# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='info',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.TextField(choices=[('OK', 'Correct'), ('RE', 'Run-time error'), ('WA', 'Wrong answer')]),
            preserve_default=True,
        ),
    ]
