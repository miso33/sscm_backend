# Generated by Django 3.2.9 on 2022-03-02 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parishes', '0001_initial'),
        ('profiles', '0004_auto_20220216_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='parish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='member', to='parishes.parish', verbose_name='Farnosť'),
        ),
    ]