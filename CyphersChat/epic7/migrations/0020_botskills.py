# Generated by Django 3.0.2 on 2020-01-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic7', '0019_notic_linkname'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill', models.CharField(max_length=30)),
            ],
        ),
    ]
