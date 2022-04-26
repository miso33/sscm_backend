# Generated by Django 3.2.9 on 2022-03-17 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20220311_1724'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='payment',
            name='payments_pa_user_id_be07d0_idx',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='member',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='profiles.memberprofile', verbose_name='Člen'),
        ),
        migrations.AddField(
            model_name='payment',
            name='year',
            field=models.IntegerField(default='2000', verbose_name='Rok'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='gift',
            field=models.BooleanField(default=False, verbose_name='Členské'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='membership',
            field=models.BooleanField(default=False, verbose_name='Dar'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['member'], name='payments_pa_member__7b306c_idx'),
        ),
    ]