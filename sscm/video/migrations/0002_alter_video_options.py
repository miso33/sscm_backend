# Generated by Django 3.2.9 on 2022-01-19 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['created']},
        ),
    ]
