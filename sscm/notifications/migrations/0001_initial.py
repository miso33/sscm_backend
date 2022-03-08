# Generated by Django 4.0.2 on 2022-02-14 10:22

import ckeditor.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('is_removed', models.BooleanField(default=False)),
                ('recipients', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('recipients_copy', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
                ('recipients_blind_copy', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
                ('subject', models.CharField(blank=True, max_length=1000)),
                ('body', ckeditor.fields.RichTextField(blank=True, max_length=1000)),
                ('body_raw', models.CharField(blank=True, max_length=1000)),
                ('attachment_file', models.FileField(null=True, upload_to='')),
                ('send_schedule', models.DateTimeField(auto_now_add=True)),
                ('attempts_max', models.PositiveSmallIntegerField(default=10)),
                ('attempts_number', models.PositiveSmallIntegerField(default=0)),
                ('last_attempt', models.DateTimeField(null=True)),
                ('sent_datetime', models.DateTimeField(null=True)),
                ('sent', models.BooleanField(default=False)),
                ('channel', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'ordering': ['-created'],
                'default_related_name': 'emails',
            },
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['created'], name='notificatio_created_5feed0_idx'),
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['sent'], name='notificatio_sent_902d06_idx'),
        ),
    ]
