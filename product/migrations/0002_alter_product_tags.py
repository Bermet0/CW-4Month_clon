# Generated by Django 3.2.5 on 2024-01-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='tags_product', to='product.Tag'),
        ),
    ]
