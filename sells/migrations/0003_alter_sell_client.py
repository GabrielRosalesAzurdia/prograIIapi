# Generated by Django 4.2.6 on 2023-10-12 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_expirationdate'),
        ('sells', '0002_sell_client_alter_sell_costs_alter_sell_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.client'),
        ),
    ]
