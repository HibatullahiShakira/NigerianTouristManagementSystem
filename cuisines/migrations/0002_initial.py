# Generated by Django 5.1.2 on 2024-11-03 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuisines', '0001_initial'),
        ('tribes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuisine',
            name='tribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tribe_states', to='tribes.tribe'),
        ),
    ]
