# Generated by Django 5.1.5 on 2025-03-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0009_building_description_en_building_description_ru_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Admission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "title_uz",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "title_ru",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "description_uz",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                (
                    "description_ru",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                (
                    "description_en",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                ("image", models.ImageField(upload_to="", verbose_name="Image")),
            ],
            options={
                "verbose_name": "Admission",
                "verbose_name_plural": "Admissions",
            },
        ),
    ]
