# Generated by Django 2.2.7 on 2019-11-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20191119_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_img',
            name='img',
            field=models.ImageField(upload_to='media/home/image'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/icon'),
        ),
    ]