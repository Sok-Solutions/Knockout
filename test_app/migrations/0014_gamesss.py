# Generated by Django 4.1.3 on 2022-11-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0013_delete_gamesss'),
    ]

    operations = [
        migrations.CreateModel(
            name='gamesss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.CharField(max_length=255)),
                ('userid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('m', models.BooleanField(default=False)),
            ],
        ),
    ]
