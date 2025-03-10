# Generated by Django 5.1.5 on 2025-03-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_alter_chairmember_options_alter_leadership_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chairmember",
            name="contact_data",
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=255,
                null=True,
                verbose_name="Contact data",
            ),
        ),
        migrations.AddField(
            model_name="chairmember",
            name="contact_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("EMAIL", "Email"),
                    ("PHONE", "Phone"),
                    ("TELEGRAM", "Telegram"),
                    ("FACEBOOK", "Facebook"),
                    ("INSTAGRAM", "Instagram"),
                    ("TWITTER", "Twitter"),
                    ("LINKEDIN", "LinkedIn"),
                    ("WEBSITE", "Website"),
                    ("YOUTUBE", "YouTube"),
                    ("OTHER", "Other"),
                ],
                db_index=True,
                max_length=255,
                null=True,
                verbose_name="Contact Type",
            ),
        ),
    ]
