# Generated by Django 5.0 on 2023-12-31 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('release_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['name', 'model', 'release_date'], name='network_pro_name_6b7f20_idx')],
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(related_name='factory_products', to='network.products')),
            ],
            options={
                'verbose_name': 'Factory',
                'verbose_name_plural': 'Factories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dept_to_supplier', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('products', models.ManyToManyField(related_name='retailer_products', to='network.products')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_supplier', to='network.factory')),
            ],
            options={
                'verbose_name': 'Retailer',
                'verbose_name_plural': 'Retailers',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='RetailerProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.products')),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.retailer')),
            ],
        ),
        migrations.CreateModel(
            name='IndividualSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dept_to_supplier', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individual_seller_supplier', to='network.retailer')),
                ('products', models.ManyToManyField(related_name='indivodual_seller_products', to='network.retailerproducts')),
            ],
            options={
                'verbose_name': 'IndividualSeller',
                'verbose_name_plural': 'IndividualSellers',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='factory',
            index=models.Index(fields=['name', 'slug', 'email', 'country', 'city'], name='network_fac_name_eafdc0_idx'),
        ),
        migrations.AddIndex(
            model_name='retailer',
            index=models.Index(fields=['name', 'slug', 'email', 'country', 'city'], name='network_ret_name_73b75e_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='retailerproducts',
            unique_together={('retailer', 'product')},
        ),
        migrations.AddIndex(
            model_name='individualseller',
            index=models.Index(fields=['name', 'slug', 'email', 'country', 'city'], name='network_ind_name_e8a50f_idx'),
        ),
    ]
