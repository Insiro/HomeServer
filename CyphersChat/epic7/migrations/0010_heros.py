# Generated by Django 3.0 on 2019-12-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic7', '0009_delete_heros'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SearchKey', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.IntegerField()),
                ('classType', models.CharField(max_length=20)),
                ('element', models.CharField(max_length=10)),
            ],
        ),
    ]
