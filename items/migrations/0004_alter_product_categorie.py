# Generated by Django 4.2.2 on 2023-06-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categorie',
            field=models.CharField(choices=[('Café', 'Café'), ('Cafféine', 'Cafféine'), ('Suppléments', 'Suppléments'), ('Espresso', 'Espresso'), ('Pâtisseries', 'Pâtisseries')], default='Pâtisseries', max_length=100),
        ),
    ]
