# Generated by Django 3.2.9 on 2022-03-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('originaldata', '0005_auto_20220216_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='originalmember',
            name='death_date',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum úmrtia'),
        ),
        migrations.AddField(
            model_name='originalmember',
            name='leave_date',
            field=models.DateField(blank=True, null=True, verbose_name='Dátum vyradenia'),
        ),
    ]
