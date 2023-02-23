# Generated by Django 4.1.7 on 2023-02-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='images/icons')),
            ],
        ),
    ]