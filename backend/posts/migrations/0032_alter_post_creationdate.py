# Generated by Django 4.1.3 on 2023-01-17 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_alter_post_creationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 4, 17, 19, 755385, tzinfo=datetime.timezone.utc)),
        ),
    ]
