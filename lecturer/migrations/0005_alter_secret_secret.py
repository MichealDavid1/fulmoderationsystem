# Generated by Django 4.0.4 on 2022-11-04 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0004_secret_wrongfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='secret',
            field=models.CharField(max_length=500),
        ),
    ]
