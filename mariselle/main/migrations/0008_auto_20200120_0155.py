# Generated by Django 2.1.11 on 2020-01-20 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_homepicture_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepicture',
            name='title',
            field=models.TextField(max_length=250),
        ),
    ]
