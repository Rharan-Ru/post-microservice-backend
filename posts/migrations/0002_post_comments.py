# Generated by Django 4.0 on 2022-01-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.TextField(default=[]),
        ),
    ]
