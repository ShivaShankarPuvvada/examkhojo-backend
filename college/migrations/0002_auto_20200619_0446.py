# Generated by Django 3.0.4 on 2020-06-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='keywords',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='meta',
            field=models.TextField(null=True),
        ),
    ]
