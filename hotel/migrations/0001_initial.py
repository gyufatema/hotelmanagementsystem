# Generated by Django 5.0.2 on 2024-03-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('king', 'KING'), ('queen', 'QUEEN'), ('ac', 'AC'), ('non-ac', 'NON-AC'), ('single', 'SINGLE'), ('double', 'DOUBLE'), ('deluxe', 'DELUXE'), ('bridalsuite', 'BRIDAL SUITE')], max_length=50)),
                ('bed', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]