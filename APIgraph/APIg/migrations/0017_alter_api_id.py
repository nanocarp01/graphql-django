# Generated by Django 3.2.7 on 2021-09-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIg', '0016_alter_api_legajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
