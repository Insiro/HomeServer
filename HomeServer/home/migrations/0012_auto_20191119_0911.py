# Generated by Django 2.2.6 on 2019-11-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
