# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vizmanager', '0004_auto_20170206_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('indicator', models.CharField(max_length=200, verbose_name='indicator')),
            ],
            options={
                'verbose_name_plural': 'Indicators',
                'verbose_name': 'Indicator',
            },
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'KPIs',
                'verbose_name': 'KPI',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(primary_key=True, serialize=False, verbose_name='Url')),
            ],
            options={
                'verbose_name_plural': 'Organizations',
                'verbose_name': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(primary_key=True, serialize=False, verbose_name='Url')),
            ],
            options={
                'verbose_name_plural': 'Budget Phases',
                'verbose_name': 'Budget Phase',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(primary_key=True, serialize=False, verbose_name='Url')),
            ],
            options={
                'verbose_name_plural': 'Years',
                'verbose_name': 'Year',
            },
        ),
        migrations.AlterField(
            model_name='dataset',
            name='viz_type',
            field=models.CharField(choices=[('Treemap', 'Treemap'), ('BarChart', 'BarChart'), ('PieChart', 'PieChart'), ('BubbleTree', 'BubbleTree'), ('Sankey', 'Sankey'), ('Radar', 'Radar'), ('PivotTable', 'PivotTable'), ('Table', 'Table')], max_length=200, verbose_name='Visualization Type'),
        ),
        migrations.AddField(
            model_name='kpi',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vizmanager.Organization'),
        ),
        migrations.AddField(
            model_name='kpi',
            name='phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vizmanager.Phase'),
        ),
        migrations.AddField(
            model_name='kpi',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vizmanager.Year'),
        ),
        migrations.AddField(
            model_name='microsite',
            name='kpi_set',
            field=models.ManyToManyField(to='vizmanager.KPI'),
        ),
    ]