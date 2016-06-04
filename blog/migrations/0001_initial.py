# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-04 16:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField(default=False)),
                ('invoice', models.IntegerField(default=2)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_type', models.CharField(max_length=200)),
                ('cart', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
                ('weight', models.FloatField()),
                ('image', models.ImageField(upload_to='%Y/%m/%d/')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.AddField(
            model_name='cart_item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Product'),
        ),
    ]
