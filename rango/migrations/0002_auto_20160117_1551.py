# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tapak',
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
            old_name='Bares',
            new_name='Barek',
        ),
        migrations.RemoveField(
            model_name='tapas',
            name='bar',
        ),
        migrations.DeleteModel(
            name='Tapas',
        ),
        migrations.AddField(
            model_name='tapak',
            name='bar',
            field=models.ForeignKey(to='rango.Barek'),
            preserve_default=True,
        ),
    ]
