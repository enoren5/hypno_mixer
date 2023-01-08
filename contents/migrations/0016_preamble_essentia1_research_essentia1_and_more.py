# Generated by Django 4.1.1 on 2023-01-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0015_rename_essential1_induction_essentia1'),
    ]

    operations = [
        migrations.AddField(
            model_name='preamble',
            name='essentia1',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='research',
            name='essentia1',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='scriptsuggestion',
            name='essentia1',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='stockscript',
            name='essentia1',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]