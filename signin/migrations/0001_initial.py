# Generated by Django 2.0.4 on 2018-05-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sign_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.IntegerField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]