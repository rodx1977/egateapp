# Generated by Django 2.0.7 on 2018-09-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egate', '0005_auto_20180906_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitado',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
    ]
