# Generated by Django 2.0.4 on 2018-06-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0004_sign_in_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_in',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
