# Generated by Django 3.2.7 on 2021-09-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIg', '0017_alter_api_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]