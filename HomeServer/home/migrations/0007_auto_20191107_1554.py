# Generated by Django 2.2.6 on 2019-11-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191106_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_img',
            name='img',
            field=models.ImageField(upload_to='image'),
        ),
    ]