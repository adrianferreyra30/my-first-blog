# Generated by Django 2.2.24 on 2021-11-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_partida'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='duracion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partida',
            name='puntos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
