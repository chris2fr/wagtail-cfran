# Generated by Django 5.0.4 on 2024-05-08 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_dsfacile", "0009_alter_dsfrconfig_footer_brand_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dsfacilesocialmedia",
            name="site_config",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="django_dsfacile.dsfacileconfig"
            ),
        ),
    ]