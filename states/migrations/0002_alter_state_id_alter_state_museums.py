# Generated by Django 5.1.3 on 2024-11-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museuems', '0002_alter_museum_id'),
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='state',
            name='museums',
            field=models.ManyToManyField(related_name='states', to='museuems.museum'),
        ),
    ]
