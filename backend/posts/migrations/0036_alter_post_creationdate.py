# Generated by Django 4.1.2 on 2023-02-08 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_alter_post_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 8, 3, 56, 14, 530804, tzinfo=datetime.timezone.utc)),
        ),
    ]