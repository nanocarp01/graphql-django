# Generated by Django 3.2.7 on 2021-09-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIg', '0008_alter_api_legajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='agente',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='api',
            name='secretaria',
            field=models.CharField(max_length=500),
        ),
    ]
