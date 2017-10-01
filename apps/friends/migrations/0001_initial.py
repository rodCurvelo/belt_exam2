# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='second_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepter', to='friends.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='user_friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='friends.User'),
        ),
    ]
