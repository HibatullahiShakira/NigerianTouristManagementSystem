# Generated by Django on 2024-11-20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='image/', null=True, blank=True)),
                ('state', models.ForeignKey(on_delete=models.PROTECT, related_name='museum_state', to='states.state')),
            ],
        ),
    ]
