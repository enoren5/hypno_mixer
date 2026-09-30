import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0029_rename_essentia1_to_essential'),
    ]

    # Grandfathered rows (everything that existed before this migration) get
    # backfilled to 1 September 2022, per preserve_default=False below. New
    # rows created from here on default to today's date instead, per the
    # `publication_date` field as declared in models.py.
    operations = [
        migrations.AddField(
            model_name='preamble',
            name='publication_date',
            field=models.DateField(default=datetime.date(2022, 9, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='induction',
            name='publication_date',
            field=models.DateField(default=datetime.date(2022, 9, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scriptsuggestion',
            name='publication_date',
            field=models.DateField(default=datetime.date(2022, 9, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='research',
            name='publication_date',
            field=models.DateField(default=datetime.date(2022, 9, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockscript',
            name='publication_date',
            field=models.DateField(default=datetime.date(2022, 9, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assortedliterature',
            name='publication_date',
            field=models.DateField(default=datetime.date(2022, 9, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='binaurals',
            name='publication_date',
            field=models.DateField(default=datetime.date(2022, 9, 1)),
            preserve_default=False,
        ),
    ]
