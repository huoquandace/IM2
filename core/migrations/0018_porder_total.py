# Generated by Django 4.2.1 on 2023-05-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_porder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='porder',
            name='total',
            field=models.IntegerField(blank=True, null=True, verbose_name='total'),
        ),
    ]
