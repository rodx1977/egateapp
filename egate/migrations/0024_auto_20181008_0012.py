# Generated by Django 2.0.7 on 2018-10-08 05:12

from django.db import migrations, models
import egate.models


class Migration(migrations.Migration):

    dependencies = [
        ('egate', '0023_auto_20181008_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitacion',
            name='cedula_invitado',
            field=models.CharField(blank=True, default=egate.models.Invitacion.cedula_default, max_length=13),
        ),
    ]