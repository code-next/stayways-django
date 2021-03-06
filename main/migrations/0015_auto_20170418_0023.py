# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 18:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_room_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.FileField(upload_to='/room/')),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='photo',
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(default='Title', max_length=255),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Room'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
