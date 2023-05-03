# Generated by Django 4.0.7 on 2023-05-03 02:09

import core.common.size
import core.common.status
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='coffees')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Coffee',
                'verbose_name_plural': 'Coffees',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('prefered_size', django_enumfield.db.fields.EnumField(default=1, enum=core.common.size.Size)),
                ('points', models.IntegerField(default=0)),
                ('status', django_enumfield.db.fields.EnumField(default=1, enum=core.common.status.Status)),
                ('favorite_coffee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.coffee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mercado_pago_data', models.JSONField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Recharge',
                'verbose_name_plural': 'Recharges',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('percentaje', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('expire_date', models.DateTimeField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('filters', models.JSONField(blank=True, null=True)),
                ('coffee_related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.coffee')),
                ('users', models.ManyToManyField(related_name='promotions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=19)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_use', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Campain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('html_content', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('objective_date', models.DateTimeField()),
                ('promotion_related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.promotion')),
                ('users', models.ManyToManyField(related_name='campains', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Campain',
                'verbose_name_plural': 'Campains',
            },
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('size', models.CharField(choices=[(1, core.common.size.Size(1)), (2, core.common.size.Size(2)), (3, core.common.size.Size(3)), (4, core.common.size.Size(4))], default=core.common.size.Size(1), max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.coffee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Buy',
                'verbose_name_plural': 'Buys',
            },
        ),
    ]
