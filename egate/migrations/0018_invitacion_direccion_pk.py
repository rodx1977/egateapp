# Generated by Django 2.0.7 on 2018-09-23 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('egate', '0017_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitacion',
            name='direccion_pk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='egate.Direccion'),
            preserve_default=False,
        ),
    ]
