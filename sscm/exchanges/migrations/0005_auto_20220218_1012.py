# Generated by Django 3.2.9 on 2022-02-18 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import model_utils.fields
import phonenumber_field.modelfields
import sscm.core.countries


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220216_1058'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchanges', '0004_auto_20220203_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('is_removed', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='Krstné meno')),
                ('last_name', models.CharField(max_length=50, verbose_name='Priezvisko')),
                ('birth_date', models.CharField(max_length=500, verbose_name='Dátum narodenia')),
                ('address', models.CharField(max_length=500, verbose_name='Adresa')),
                ('home_country', django_countries.fields.CountryField(countries=sscm.core.countries.ExchangeCountries, max_length=2, verbose_name='Domáca krajina')),
                ('residence_country', django_countries.fields.CountryField(countries=sscm.core.countries.ExchangeCountries, max_length=2, verbose_name='Krajina pobytu')),
                ('academic_year', models.IntegerField(blank=True, null=True, verbose_name='Školský rok pobytu')),
                ('semester', models.CharField(blank=True, choices=[('WINTER', 'Zimný'), ('SUMMER', 'Letný')], default='WINTER', max_length=10, verbose_name='Polrok pobytu')),
                ('start', models.DateField(null=True, verbose_name='Dátum začiatku')),
                ('end', models.DateField(null=True, verbose_name='Dátum konca')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Mobilné číslo')),
                ('university_name', models.CharField(blank=True, max_length=500, verbose_name='Univerzita názov')),
                ('university_country', django_countries.fields.CountryField(blank=True, countries=sscm.core.countries.ExchangeCountries, max_length=2)),
                ('study_filed', models.CharField(blank=True, max_length=500, verbose_name='Študijný odbor')),
                ('profession', models.CharField(blank=True, max_length=500, verbose_name='Povolanie')),
                ('language', models.JSONField(verbose_name='Jazyky')),
                ('title_prefix', models.CharField(blank=True, max_length=50, verbose_name='Titul pred menom')),
                ('title_suffix', models.CharField(blank=True, max_length=50, verbose_name='Titul za menom')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Dátum úmrtia')),
                ('foreign_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreign_students', to='exchanges.school', verbose_name='Zahraničná škola')),
                ('home_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_students', to='exchanges.school', verbose_name='Domáca škola')),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='profiles.memberprofile', verbose_name='Člen')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL, verbose_name='Užívateľské konto')),
            ],
            options={
                'verbose_name': 'Študent',
                'verbose_name_plural': 'Študenti',
                'ordering': ['-created'],
                'default_related_name': 'students',
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddIndex(
            model_name='studentprofile',
            index=models.Index(fields=['last_name'], name='exchanges_s_last_na_d0ead6_idx'),
        ),
        migrations.AddIndex(
            model_name='studentprofile',
            index=models.Index(fields=['semester'], name='exchanges_s_semeste_8e4354_idx'),
        ),
        migrations.AddIndex(
            model_name='studentprofile',
            index=models.Index(fields=['home_country'], name='exchanges_s_home_co_3e7711_idx'),
        ),
        migrations.AddIndex(
            model_name='studentprofile',
            index=models.Index(fields=['residence_country'], name='exchanges_s_residen_f1986b_idx'),
        ),
        migrations.AddIndex(
            model_name='studentprofile',
            index=models.Index(fields=['birth_date'], name='exchanges_s_birth_d_7b8b1d_idx'),
        ),
    ]