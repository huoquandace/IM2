# Generated by Django 4.2.1 on 2023-05-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_supplier_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='core.product', verbose_name='products'),
        ),
    ]
