# Generated by Django 4.1.6 on 2023-02-08 02:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0006_categorydepth1_categorydepth2_categorydepth3_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categorydepth1",
            options={
                "verbose_name": "Category (Depth 1)",
                "verbose_name_plural": "Categories (Depth 1)",
            },
        ),
        migrations.AlterModelOptions(
            name="categorydepth2",
            options={
                "verbose_name": "Category (Depth 2)",
                "verbose_name_plural": "Categories (Depth 2)",
            },
        ),
        migrations.AlterModelOptions(
            name="categorydepth3",
            options={
                "verbose_name": "Category (Depth 3)",
                "verbose_name_plural": "Categories (Depth 3)",
            },
        ),
        migrations.AlterField(
            model_name="categorydepth1",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="categorydepth2",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="categorydepth3",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]
