# Generated by Django 5.0.6 on 2024-06-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_releasecoure_course_price_releasecoure_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasecoure',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
