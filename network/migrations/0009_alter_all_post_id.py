# Generated by Django 4.1.3 on 2022-12-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_alter_all_post_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_post',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]