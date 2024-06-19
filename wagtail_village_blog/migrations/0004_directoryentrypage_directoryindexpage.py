# Generated by Django 5.0.6 on 2024-06-18 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_village_blog", "0003_alter_category_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="DirectoryEntryPage",
            fields=[
                (
                    "blogentrypage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtail_village_blog.blogentrypage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Entry",
                "verbose_name_plural": "Entries",
            },
            bases=("wagtail_village_blog.blogentrypage",),
        ),
        migrations.CreateModel(
            name="DirectoryIndexPage",
            fields=[
                (
                    "blogindexpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtail_village_blog.blogindexpage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Base page",
                "verbose_name_plural": "Base pages",
                "abstract": False,
            },
            bases=("wagtail_village_blog.blogindexpage",),
        ),
    ]
