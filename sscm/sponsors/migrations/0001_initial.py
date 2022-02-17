# Generated by Django 3.2.9 on 2022-02-02 17:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import model_utils.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('is_removed', models.BooleanField(default=False)),
                ('date', models.DateField(verbose_name='Dátum')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Suma')),
                ('note', models.CharField(max_length=500, verbose_name='Poznámka')),
                ('currency', models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dolár')], default='EUR', max_length=20, verbose_name='Mena')),
                ('method', models.CharField(choices=[('CASH', 'Hotovosť'), ('TRANSFER', 'Prevod na účet')], default='CASH', max_length=20, verbose_name='Platobná metóda')),
            ],
            options={
                'verbose_name': 'Sponzor',
                'verbose_name_plural': 'Sponzori',
                'ordering': ['-created'],
                'default_related_name': 'payments',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('is_removed', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='Krstné meno')),
                ('last_name', models.CharField(max_length=30, verbose_name='Priezvisko')),
                ('birth_date', models.CharField(max_length=500, verbose_name='Dátum narodenia')),
                ('address', models.CharField(blank=True, max_length=500, verbose_name='Adresa')),
                ('city', models.CharField(blank=True, max_length=500, verbose_name='Mesto')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('email', models.CharField(max_length=500, verbose_name='Adresa')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=500, region=None, verbose_name='Adresa')),
                ('profession', models.CharField(max_length=500, verbose_name='Adresa')),
                ('account_number', models.CharField(blank=True, max_length=500, verbose_name='Adresa')),
                ('language', models.CharField(max_length=500, verbose_name='Jazyk')),
            ],
            options={
                'verbose_name': 'Sponzor',
                'verbose_name_plural': 'Sponzori',
                'ordering': ['last_name'],
                'default_related_name': 'sponsors',
            },
        ),
        migrations.AddIndex(
            model_name='sponsor',
            index=models.Index(fields=['first_name'], name='sponsors_sp_first_n_d77246_idx'),
        ),
        migrations.AddIndex(
            model_name='sponsor',
            index=models.Index(fields=['last_name'], name='sponsors_sp_last_na_536199_idx'),
        ),
        migrations.AddField(
            model_name='payment',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='sponsors.sponsor', verbose_name='Sponzor'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['sponsor'], name='sponsors_pa_sponsor_10c018_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['currency'], name='sponsors_pa_currenc_17a2ec_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['method'], name='sponsors_pa_method_50cd7c_idx'),
        ),
    ]
