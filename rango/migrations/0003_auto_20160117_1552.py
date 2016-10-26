# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160117_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tapas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('votos', models.IntegerField(default=0)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Barek',
            new_name='Bares',
        ),
        migrations.RemoveField(
            model_name='tapak',
            name='bar',
        ),
        migrations.DeleteModel(
            name='Tapak',
        ),
        migrations.AddField(
            model_name='tapas',
            name='bar',
            field=models.ForeignKey(to='rango.Bares'),
            preserve_default=True,
        ),
    ]
