# Generated by Django 5.0.6 on 2024-05-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('Skilled_Instructors', models.CharField(max_length=400)),
                ('SkilledDescription', models.TextField()),
                ('International_Certificate', models.CharField(max_length=600)),
                ('InternationalDescription', models.TextField()),
                ('Online_Classes', models.CharField(max_length=600)),
                ('OnlineDescription', models.TextField()),
                ('image', models.ImageField(upload_to='feature_images/')),
            ],
        ),
    ]
