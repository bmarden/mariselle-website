# Generated by Django 2.1.11 on 2020-01-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190809_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepicture',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
