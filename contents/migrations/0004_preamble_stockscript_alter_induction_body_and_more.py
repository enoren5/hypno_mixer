# Generated by Django 4.1.1 on 2022-09-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_research_author_research_body_research_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preamble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('body', models.TextField(blank=True, max_length=300000)),
                ('author', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StockScript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('body', models.TextField(blank=True, max_length=300000)),
                ('author', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='induction',
            name='body',
            field=models.TextField(blank=True, max_length=300000),
        ),
        migrations.AlterField(
            model_name='induction',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='research',
            name='author',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='research',
            name='body',
            field=models.TextField(blank=True, max_length=300000),
        ),
        migrations.AlterField(
            model_name='research',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='scriptsuggestions',
            name='author',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='scriptsuggestions',
            name='body',
            field=models.TextField(blank=True, max_length=300000),
        ),
        migrations.AlterField(
            model_name='scriptsuggestions',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]