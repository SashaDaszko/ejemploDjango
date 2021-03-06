# Generated by Django 3.2.9 on 2021-12-08 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_jugador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=40)),
                ('anioFund', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='esNoche',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='esBueno',
            field=models.BooleanField(null=True),
        ),
    ]
