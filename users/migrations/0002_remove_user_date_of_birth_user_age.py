# Generated by Django 5.1.3 on 2024-11-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(default=18),
            preserve_default=False,
        ),
    ]