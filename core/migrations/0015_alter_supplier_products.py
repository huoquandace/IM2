# Generated by Django 4.2.1 on 2023-05-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_porder_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='products',
            field=models.ManyToManyField(blank=True, to='core.product', verbose_name='products'),
        ),
    ]
