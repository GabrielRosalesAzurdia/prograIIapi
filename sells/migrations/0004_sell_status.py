# Generated by Django 4.2.6 on 2023-10-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0003_alter_sell_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
