# Generated by Django 5.0.5 on 2024-09-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appin5", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Datas",
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
                ("Name", models.CharField(default="", max_length=20)),
                ("Age", models.IntegerField(default="")),
                ("Address", models.CharField(default="", max_length=50)),
                ("Mail", models.CharField(default="", max_length=50)),
            ],
        ),
    ]
