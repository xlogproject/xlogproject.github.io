# Generated by Django 4.1.2 on 2023-03-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_followeduser_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/profiles'),
        ),
    ]
