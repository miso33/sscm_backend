# Generated by Django 3.2.9 on 2021-11-29 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('originaldata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='originalmember',
            options={'default_related_name': 'original_member', 'ordering': ['surname'], 'verbose_name': 'Pôvodný údaj členov', 'verbose_name_plural': 'Pôvodné údaje členov'},
        ),
    ]