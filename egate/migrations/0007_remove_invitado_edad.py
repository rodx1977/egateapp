# Generated by Django 2.0.7 on 2018-09-07 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egate', '0006_auto_20180906_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitado',
            name='edad',
        ),
    ]
