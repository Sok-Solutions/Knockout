# Generated by Django 4.1.3 on 2022-11-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0009_gamesss_delete_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('withname', models.BooleanField(default=False)),
            ],
        ),
    ]