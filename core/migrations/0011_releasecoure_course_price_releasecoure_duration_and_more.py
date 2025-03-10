# Generated by Django 5.0.6 on 2024-06-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_newslettersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasecoure',
            name='course_price',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='releasecoure',
            name='duration',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='releasecoure',
            name='language',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='releasecoure',
            name='lectures',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='releasecoure',
            name='skill_level',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
