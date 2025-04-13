# Generated by Django 5.2 on 2025-04-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %'),
        ),
    ]
