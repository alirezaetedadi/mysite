# Generated by Django 2.0.4 on 2018-05-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0002_auto_20180522_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_in',
            name='password',
            field=models.IntegerField(),
        ),
    ]
