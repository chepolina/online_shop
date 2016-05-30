# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 16:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20160514_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='payment',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Payment'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
