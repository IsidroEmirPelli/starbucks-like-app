# Generated by Django 4.0.7 on 2023-05-15 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_userprofile_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="campain",
            name="subject",
            field=models.CharField(default="", max_length=100),
        ),
    ]
