# Generated by Django 2.0.4 on 2018-06-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0003_auto_20180526_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign_in',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
