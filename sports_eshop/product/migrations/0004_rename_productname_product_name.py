# Generated by Django 4.2.3 on 2024-02-06 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_options_product_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='name',
        ),
    ]
