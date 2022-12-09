# Generated by Django 4.1.3 on 2022-12-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_anime_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]