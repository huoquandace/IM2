# Generated by Django 4.2.1 on 2023-05-27 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('label', models.CharField(max_length=255, verbose_name='label')),
                ('image', models.ImageField(upload_to='category', verbose_name='image')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.CharField(max_length=255, verbose_name='product id')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('brand', models.CharField(max_length=255, verbose_name='brand')),
                ('image', models.ImageField(upload_to='product', verbose_name='image')),
                ('description', models.TextField(verbose_name='description')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]