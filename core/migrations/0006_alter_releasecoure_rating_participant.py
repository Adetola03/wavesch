# Generated by Django 5.0.6 on 2024-06-05 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_releasecoure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releasecoure',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.releasecoure')),
            ],
        ),
    ]
