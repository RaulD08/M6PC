# Generated by Django 4.0.5 on 2023-07-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0007_colormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colormodel',
            name='color',
            field=models.CharField(choices=[('Azul', 'Azul'), ('Morado', 'Morado'), ('Verde', 'Verde'), ('AzulD', 'Azul'), ('MoradoD', 'MoradoD'), ('VerdeD', 'Verde')], max_length=20),
        ),
    ]
