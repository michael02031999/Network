# Generated by Django 4.1.3 on 2022-12-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=500)),
                ('comment', models.TextField(max_length=500)),
                ('date', models.TextField(max_length=500)),
                ('time', models.TextField(max_length=500)),
                ('likes', models.IntegerField()),
            ],
        ),
    ]
