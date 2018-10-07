# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('value', models.CharField(max_length=32, verbose_name='token值')),
                ('time', models.IntegerField(verbose_name='token寿命')),
                ('create_time', models.DateTimeField(verbose_name='token创建时间')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
            ],
        ),
    ]
