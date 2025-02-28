# Generated by Django 5.1.5 on 2025-02-28 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0006_chairmember"),
    ]

    operations = [
        migrations.CreateModel(
            name="LaboratoryGallery",
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
                (
                    "image",
                    models.ImageField(
                        upload_to="laboratory/gallery/", verbose_name="Image"
                    ),
                ),
                (
                    "laboratory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="laboratory_galleries",
                        to="backend.laboratory",
                        verbose_name="Laboratory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Laboratory Gallery",
                "verbose_name_plural": "Laboratory Galleries",
                "ordering": ("-created_at",),
            },
        ),
    ]
