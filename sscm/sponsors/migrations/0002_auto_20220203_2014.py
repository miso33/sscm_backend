# Generated by Django 3.2.9 on 2022-02-03 19:14

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'default_related_name': 'payments', 'ordering': ['-created'], 'verbose_name': 'Platba', 'verbose_name_plural': 'Platby'},
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='account_number',
            field=models.CharField(blank=True, max_length=500, verbose_name='Číslo účtu'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='birth_date',
            field=models.DateField(verbose_name='Dátum narodenia'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='email',
            field=models.CharField(max_length=500, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=500, region=None, verbose_name='Telefónne číslo'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='profession',
            field=models.CharField(max_length=500, verbose_name='Povolanie'),
        ),
    ]
