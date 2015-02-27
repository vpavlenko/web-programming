# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.TextField()),
                ('statement', models.TextField()),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('code', models.TextField()),
                ('status', models.TextField(choices=[('OK', 'OK'), ('ER', 'Error')])),
                ('problem', models.ForeignKey(to='lessons.Problem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.IntegerField(unique=True)),
                ('input', models.TextField()),
                ('answer', models.TextField()),
                ('problem', models.ForeignKey(to='lessons.Problem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
