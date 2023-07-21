# Generated by Django 4.0.5 on 2023-07-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0008_alter_colormodel_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='colormodel',
            name='color5',
            field=models.CharField(default='#202020', max_length=30),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='color',
            field=models.CharField(choices=[('Azul', 'Azul'), ('Morado', 'Morado'), ('Verde', 'Verde'), ('AzulD', 'AzulD'), ('MoradoD', 'MoradoD'), ('VerdeD', 'VerdeD')], default='Azul', max_length=20),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='color1',
            field=models.CharField(default='#EFF7FB', max_length=30),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='color2',
            field=models.CharField(default='#1D5B79', max_length=30),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='color3',
            field=models.CharField(default='#3093C5', max_length=30),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='color4',
            field=models.CharField(default='#f5f5f5', max_length=30),
        ),
    ]
