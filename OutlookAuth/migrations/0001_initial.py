# Generated by Django 4.2.6 on 2023-10-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('user_name',
                 models.CharField(
                     max_length=30)),
                ('email',
                 models.CharField(
                     max_length=50)),
            ],
        ),
    ]
