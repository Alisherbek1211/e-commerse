# Generated by Django 4.1.5 on 2023-02-12 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Category name')),
                ('name_en', models.CharField(blank=True, max_length=150, null=True, verbose_name='Category name')),
                ('name_uz', models.CharField(blank=True, max_length=150, null=True, verbose_name='Category name')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category ',
                'verbose_name_plural': 'Categories ',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Product name')),
                ('name_en', models.CharField(max_length=400, null=True, verbose_name='Product name')),
                ('name_uz', models.CharField(max_length=400, null=True, verbose_name='Product name')),
                ('image', models.ImageField(upload_to='product-images', verbose_name='Product image')),
                ('description', models.TextField(verbose_name='Product description')),
                ('description_en', models.TextField(null=True, verbose_name='Product description')),
                ('description_uz', models.TextField(null=True, verbose_name='Product description')),
                ('price', models.IntegerField(verbose_name='Product price')),
                ('discount', models.IntegerField(default=0, verbose_name='Product discount')),
                ('category', models.ManyToManyField(related_name='products', to='products.category', verbose_name='Choose category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product ',
                'verbose_name_plural': 'Products ',
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paket', to='products.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product-albums')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rasmlar', to='products.product')),
            ],
        ),
    ]
