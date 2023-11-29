# Generated by Django 4.2.7 on 2023-11-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='false', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank='false', max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]