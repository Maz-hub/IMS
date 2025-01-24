# Generated by Django 5.1.5 on 2025-01-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('origin_country', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('approx_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
