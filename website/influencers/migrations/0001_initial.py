# Generated by Django 4.0.3 on 2022-03-16 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfluencer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_email', models.EmailField(max_length=254)),
                ('influencer_name', models.CharField(max_length=255)),
                ('influencer_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('influencer_name', models.CharField(max_length=255)),
                ('influencer_email', models.EmailField(default='example@gmail.com', max_length=254)),
                ('youtube_channel_id', models.CharField(default='Add You Channel Id here', max_length=255)),
                ('influencer_short_description', models.TextField()),
                ('profile_photo', models.ImageField(upload_to='media/ytubers/%Y/%m/')),
                ('category', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
