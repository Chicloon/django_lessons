# Generated by Django 4.1.7 on 2023-03-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquirer_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquirer',
            name='time',
            field=models.IntegerField(default=10),
        ),
    ]
