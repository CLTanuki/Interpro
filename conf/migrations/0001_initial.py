# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conf',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=20)),
                ('alias', models.CharField(unique=True, verbose_name='Alias', max_length=25)),
                ('date', models.DateField(verbose_name='Date')),
                ('schedule', models.TextField(verbose_name='Shedule')),
                ('thesis_rules', models.TextField(verbose_name='Thesis Rules')),
                ('orgs', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Managers')),
                ('place', models.ForeignKey(to='enterprise.CorpObject', verbose_name='Place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfMember',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_reporter', models.BooleanField(default=False, verbose_name='Reporter')),
                ('conf', models.ForeignKey(to='Conf.Conf')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
