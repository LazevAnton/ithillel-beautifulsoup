# Generated by Django 4.2 on 2023-04-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_poster', models.URLField()),
                ('title', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]