# Generated by Django 2.2.6 on 2019-11-08 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_careers_myinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='context',
            field=models.TextField(blank=True, null=True),
        ),
    ]