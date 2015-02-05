# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='eml',
            field=models.CharField(default=b'email', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='msg',
            field=models.CharField(default=datetime.datetime(2015, 2, 4, 23, 54, 12, 422765, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
