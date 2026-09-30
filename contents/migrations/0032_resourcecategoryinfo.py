from django.db import migrations, models


def seed_resource_categories(apps, schema_editor):
    ResourceCategoryInfo = apps.get_model('contents', 'ResourceCategoryInfo')
    for category, _label in (
        ('inductions', 'Inductions'),
        ('custom_scripts', 'Customized Scripts'),
        ('stock_scripts', 'Base / Source Scripts'),
        ('binaurals', 'Binaural Audio Files'),
    ):
        ResourceCategoryInfo.objects.get_or_create(category=category)


def unseed_resource_categories(apps, schema_editor):
    ResourceCategoryInfo = apps.get_model('contents', 'ResourceCategoryInfo')
    ResourceCategoryInfo.objects.filter(
        category__in=['inductions', 'custom_scripts', 'stock_scripts', 'binaurals']
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0031_publication_date_default_today'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceCategoryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('inductions', 'Inductions'), ('custom_scripts', 'Customized Scripts'), ('stock_scripts', 'Base / Source Scripts'), ('binaurals', 'Binaural Audio Files')], max_length=20, unique=True)),
                ('info_text', models.TextField(blank=True, help_text="Shown in the info bubble next to this category's heading on the resources page.")),
            ],
            options={
                'verbose_name': 'Resource Category Info',
                'verbose_name_plural': 'Resource Category Info',
            },
        ),
        migrations.RunPython(seed_resource_categories, unseed_resource_categories),
    ]
