# Generated by Django 4.0.5 on 2023-07-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0005_vehiculomodel_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='vehiculos/'),
        ),
    ]
