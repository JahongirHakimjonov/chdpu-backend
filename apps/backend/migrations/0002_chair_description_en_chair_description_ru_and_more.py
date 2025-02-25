# Generated by Django 5.1.5 on 2025-02-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chair",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="chair",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="chair",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="chair",
            name="name_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="chair",
            name="name_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="chair",
            name="name_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="chair",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="chair",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="chair",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="cooperation",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="cooperation",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="cooperation",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="cooperation",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="cooperation",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="cooperation",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="info",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="info",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="info",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="info",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="info",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="info",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="interview",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="interview",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="interview",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="interview",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="interview",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="interview",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="laboratory",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="laboratory",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="laboratory",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="laboratory",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="laboratory",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="laboratory",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="name_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="name_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="name_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="leadership",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="news",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="news",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="news",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="news",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="news",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="news",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="student",
            name="description_en",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="student",
            name="description_ru",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="student",
            name="description_uz",
            field=models.TextField(null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="student",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="student",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
        migrations.AddField(
            model_name="student",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Title"),
        ),
    ]
