# Generated by Django 4.0.7 on 2023-05-09 02:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_buy_price_alter_buy_quantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buy",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100000),
                ],
            ),
        ),
    ]
