# Generated by Django 2.2.1 on 2019-05-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_date', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_photo', models.CharField(max_length=30)),
            ],
        ),
    ]
