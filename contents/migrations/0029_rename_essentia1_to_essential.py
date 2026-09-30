from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0028_article_excluded_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='induction',
            old_name='essentia1',
            new_name='essential',
        ),
        migrations.RenameField(
            model_name='scriptsuggestion',
            old_name='essentia1',
            new_name='essential',
        ),
        migrations.RenameField(
            model_name='research',
            old_name='essentia1',
            new_name='essential',
        ),
        migrations.RenameField(
            model_name='stockscript',
            old_name='essentia1',
            new_name='essential',
        ),
        migrations.RenameField(
            model_name='nytimes',
            old_name='essentia1',
            new_name='essential',
        ),
        migrations.RenameField(
            model_name='torstar',
            old_name='essentia1',
            new_name='essential',
        ),
        migrations.RenameField(
            model_name='wsjournal',
            old_name='essentia1',
            new_name='essential',
        ),
    ]
