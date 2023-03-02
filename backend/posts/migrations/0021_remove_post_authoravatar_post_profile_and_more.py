# Generated by Django 4.1.3 on 2023-01-07 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_profile_image'),
        ('posts', '0020_alter_post_creationdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='authorAvatar',
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 7, 11, 20, 42, 745446, tzinfo=datetime.timezone.utc)),
        ),
    ]
