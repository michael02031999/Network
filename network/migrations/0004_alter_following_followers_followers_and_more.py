# Generated by Django 4.1.3 on 2022-12-10 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_following_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following_followers',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='following_followers',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]