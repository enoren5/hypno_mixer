from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0026_drop_geeks_field'),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE contents_research DROP COLUMN IF EXISTS geeks_field;",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]