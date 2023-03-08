# Generated by Django 4.1.6 on 2023-02-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0004_lvl1category_full_code_lvl2category_full_code_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lvl1category",
            name="full_code",
        ),
        migrations.RemoveField(
            model_name="lvl2category",
            name="full_code",
        ),
        migrations.RemoveField(
            model_name="lvl3category",
            name="full_code",
        ),
        migrations.AlterField(
            model_name="lvl3category",
            name="code",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
