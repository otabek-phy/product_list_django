# Generated by Django 5.1.6 on 2025-03-05 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('rating', models.PositiveIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
