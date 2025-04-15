# Generated by Django 4.2.9 on 2025-04-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HideShowFilter",
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
                ("parent", models.CharField(blank=True, max_length=255, null=True)),
                ("key", models.CharField(max_length=255)),
                ("value", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="ModelFilter",
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
                ("parent", models.CharField(blank=True, max_length=255, null=True)),
                ("key", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="PageItems",
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
                ("parent", models.CharField(blank=True, max_length=255, null=True)),
                ("items_per_page", models.IntegerField(default=25)),
            ],
        ),
    ]
