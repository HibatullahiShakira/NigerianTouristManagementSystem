# Generated by Django on 2024-11-20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        #('tribes', '0001_initial'),
        ('museuems', '0001_initial'),
        ('cuisines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('geopolitical_zones', models.CharField(
                    choices=[('North Central', 'North Central'), ('North East', 'North East'),
                             ('North West', 'North West'), ('South East', 'South East'), ('South South', 'South South'),
                             ('South West', 'South West')], max_length=15)),
                ('museums', models.ManyToManyField(related_name='states', to='museums.Museum')),
                ('tribes', models.ManyToManyField(related_name='states', to='tribes.Tribe')),
            ],
        ),
    ]
