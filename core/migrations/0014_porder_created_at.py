# Generated by Django 4.2.1 on 2023-05-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_porderdetail_porder_alter_porderdetail_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='porder',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]