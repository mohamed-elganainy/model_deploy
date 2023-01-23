# Generated by Django 4.1.5 on 2023-01-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_features"),
    ]

    operations = [
        migrations.RenameField(
            model_name="features",
            old_name="f1",
            new_name="gdp",
        ),
        migrations.AddField(
            model_name="features",
            name="population",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
