# Generated by Django 4.1.7 on 2023-03-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='musics',
            field=models.ManyToManyField(related_name='musics', to='app.music'),
        ),
    ]
