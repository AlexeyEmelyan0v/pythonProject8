# Generated by Django 4.1.3 on 2022-11-26 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateTimeField(verbose_name='birth_date')),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(verbose_name='release_date')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.director')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.studio')),
            ],
        ),
    ]
