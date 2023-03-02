# Generated by Django 4.1.3 on 2023-01-10 04:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0024_rename_userreceiving_likedposts_userliked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedposts',
            name='userLiking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postsIliked', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 4, 5, 7, 904840, tzinfo=datetime.timezone.utc)),
        ),
    ]
