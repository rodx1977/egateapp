# Generated by Django 2.0.7 on 2018-09-09 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egate', '0013_invitado_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitado',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
    ]
