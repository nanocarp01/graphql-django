# Generated by Django 3.2.7 on 2021-09-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIg', '0004_alter_api_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIad',
            fields=[
                ('legajo', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_larga', models.CharField(max_length=100)),
                ('importe', models.FloatField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='API',
        ),
    ]
