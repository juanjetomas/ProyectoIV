# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20160117_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='bares',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
