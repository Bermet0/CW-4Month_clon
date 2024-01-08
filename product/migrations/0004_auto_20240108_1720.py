# Generated by Django 3.2.5 on 2024-01-08 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_order',
            name='product',
        ),
        migrations.AddField(
            model_name='product_order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.customer'),
        ),
    ]
