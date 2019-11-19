# Generated by Django 2.1.1 on 2019-09-18 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='show_pro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project_img',
            name='img',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projects',
            name='context',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='icon',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]